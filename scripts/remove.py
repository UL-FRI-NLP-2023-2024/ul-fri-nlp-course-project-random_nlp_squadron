from lxml import etree
import argparse

parser = argparse.ArgumentParser(description='Remove duplicate items from an XML file.')
parser.add_argument('dataset_path')
parser.add_argument('input_file')
args = parser.parse_args()


tree = etree.parse(f'{args.dataset_path}/{args.input_file}')
root = tree.getroot()

# Create a dictionary to store unique content
unique_content = {}
for item in root.xpath('//item'):
    content = item.find('content').text.strip()
    # Store the content in the dictionary if it's not already present
    if content not in unique_content:
        unique_content[content] = item

# Clear the root element
root.clear()

# Append unique items back to the root
for item in unique_content.values():
    root.append(item)

# Write the modified tree to the output file
tree.write(f'{args.dataset_path}/d_{args.input_file}', encoding='utf-8', xml_declaration=True)
