import copy
import xml.etree.ElementTree as ET
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

INPUT_FILE = '../../data/d_output_siol_2024-04-30T06-23-59.xml'
OUTPUT_FILE = 'output.xml'

# Define the function to calculate perplexity
def calculate_perplexity(text, model, tokenizer):
    encodings = tokenizer(text, return_tensors='pt')
    input_ids = encodings.input_ids.to(device)
    
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss
        perplexity = torch.exp(loss)
    
    return perplexity.item()

# Define the function to calculate fluency score
def fluency_score(perplexity, min_perplexity, max_perplexity):
    # Normalize perplexities to get fluency scores between 0 and 1
    score = (max_perplexity - perplexity) / (max_perplexity - min_perplexity)
    return score

def quality_score(text):
    if len(text) < 100:
        return "short"
    elif len(text) < 150:
        return "neargood"
    elif len(text) < 250:
        return "good"
    elif len(text) < 300:
        return "neargood"

# Load pre-trained model and tokenizer
model_name = 'gpt2'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = GPT2LMHeadModel.from_pretrained(model_name).to(device)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# First pass: calculate length of tree
context = ET.iterparse(INPUT_FILE, events=('end',))
counter1 = 0

for event, elem in context:
    if elem.tag == 'content':
      counter1 += 1

print(counter1)

# Initialize variables for tracking min and max perplexities
perplexities = []

# First pass: calculate perplexities and find min and max values
context = ET.iterparse(INPUT_FILE, events=('end',))
counter2 = 0

for event, elem in context:
    if elem.tag == 'content':
        print(str(counter2) + "/" + str(counter1))
        counter2 += 1
        text = elem.text
        perplexity = calculate_perplexity(text, model, tokenizer)
        perplexities.append(perplexity)
        elem.clear()

min_perplexity = min(perplexities)
max_perplexity = max(perplexities)

# Second pass: calculate fluency scores and write to a new XML
context = ET.iterparse(INPUT_FILE, events=('start', 'end'))
root = None
new_root = None
items = []

for event, elem in context:
    if event == 'start' and root is None:
        root = elem
        new_root = ET.Element(root.tag, root.attrib)
    
    if event == 'end' and elem.tag == 'item':
        content_elem = elem.find('content')
        if content_elem is not None:
            text = content_elem.text
            perplexity = calculate_perplexity(text, model, tokenizer)
            score = fluency_score(perplexity, min_perplexity, max_perplexity)

            fluency_score_elem = ET.Element('fluency_score')
            fluency_score_elem.text = str(score)
            elem.append(fluency_score_elem)

            quality = quality_score(text)
            quality_score_elem = ET.Element('quality_score')
            quality_score_elem.text = quality
            elem.append(quality_score_elem)

        # Make a deep copy of the element before clearing it
        new_elem = copy.deepcopy(elem)
        new_root.append(new_elem)
        elem.clear()

# Write the modified XML to a new file
tree = ET.ElementTree(new_root)
tree.write(OUTPUT_FILE, encoding='UTF-8', xml_declaration=True)