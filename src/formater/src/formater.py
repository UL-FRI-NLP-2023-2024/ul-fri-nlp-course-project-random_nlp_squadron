import xml.etree.ElementTree as ET
import sys

def transform_xml(input_file, output_file):
    # Load and parse the input XML file

    print(input_file)
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    # Create a new XML tree for the output
    new_root = ET.Element('root')
    
    for i, item in enumerate(root.findall('item')):
        doc = ET.SubElement(new_root, 'doc')
        doc.set('id', f"{input_file}.{i+1}")
        # doc.set('title', "Telegram: Contact @banggoodslovenija")
        doc.set('crawl_date', item.find('timestamp').text)
        doc.set('lang_distr', "[('sl', 1.0)]")
        doc.set('url', item.find('url').text)
        doc.set('domain', item.find('domain').text)
        doc.set('file_type', "html")
        
        content = item.find('content').text
        p = ET.SubElement(doc, 'p')
        p.set('id', f"{input_file}.{i+1}.1")
        # p.set('quality', "good")
        # p.set('lm_score', "0.648")
        # p.set('sensitive', "no")
        p.set('lang', "sl")
        p.text = content
    
    # Write the new tree to the output file
    tree = ET.ElementTree(new_root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <inputfile.xml> <outputfile.xml>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        transform_xml(input_file, output_file)
