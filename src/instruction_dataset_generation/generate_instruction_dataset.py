from typing import List, Optional
import json
import fire
from deep_translator import GoogleTranslator
from llama import Dialog, Llama
from lxml import etree


def parse_and_filter_xml(input_file: str) -> List[str]:
    context = etree.iterparse(input_file, events=("end",), tag="item")
    contents = []

    for event, elem in context:
        quality = elem.findtext("quality_score")
        content = elem.findtext("content").strip() if elem.findtext("content") else ""
        
        # Assuming "good" quality corresponds to content you want to keep
       
        #if quality == "good" and len(content) <= 200:
        contents.append(content)
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]

    # Take only the first 1000 contents
    top_contents = contents[:50000]

    return top_contents


def main(
    ckpt_dir: str,
    tokenizer_path: str,
    input_xml: str,
    output_file: str = "alpaca_format2.json",
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 1024,
    max_batch_size: int = 16,
    max_gen_len: Optional[int] = None,
):
    """
    Generates questions for filtered texts in Slovenian, translates the responses back to Slovenian,
    and saves the outputs in Alpaca format.
    """

    # Parse and filter the XML file
    slovenian_texts = parse_and_filter_xml(input_xml)

    # Instruction to append to each text
    instruction_text = "Generate a question in English that can be answered by the provided text. Ensure the text is a suitable response to the question. Output only the question."

    # Append the instruction to each text for generation purposes
    slovenian_texts_with_instructions = [text + instruction_text for text in slovenian_texts]

    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    translator = GoogleTranslator(source='en', target='sl')

    # Process texts in batches
    def batch(iterable, n=1):
        l = len(iterable)
        for ndx in range(0, l, n):
            yield iterable[ndx:min(ndx + n, l)]

    with open(output_file, 'w', encoding='utf-8') as f:
        alpaca_data = []

        for batch_texts in batch(slovenian_texts_with_instructions, max_batch_size):
            dialogs: List[Dialog] = [
                [{"role": "user", "content": text}] for text in batch_texts
            ]

            results = generator.chat_completion(
                dialogs,
                max_gen_len=max_gen_len,
                temperature=temperature,
                top_p=top_p,
            )

            for dialog, result in zip(dialogs, results):
                input_text_with_instruction = dialog[0]['content']
                input_text = input_text_with_instruction.replace(instruction_text, "")
                generated_text = result['generation']['content']
                translated_text = translator.translate(generated_text)
                
                alpaca_entry = {
                    "instruction": translated_text,
                    "input": "",
                    "output": input_text
                }
                alpaca_data.append(alpaca_entry)
                print(f"User: {input_text}\n")
                print(f"> Assistant: {translated_text}\n")
                print("\n==================================\n")

                # Write the entry to the JSON file incrementally
                f.seek(0)
                f.truncate()
                json.dump(alpaca_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    fire.Fire(main)

