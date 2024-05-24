import xml.etree.ElementTree as ET
import csv

def xml_to_csv(xml_file, csv_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["domain", "url", "content"])

        # Iterate over each item in the XML and write to the CSV
        for item in root.findall('item'):
            domain = item.find('domain').text
            url = item.find('url').text
            content = item.find('content').text
            writer.writerow([domain, url, content])

# Usage
xml_file = 'output.xml'  # Replace with the path to your XML file
csv_file = 'output.csv'  # Replace with the desired path for the output CSV file
xml_to_csv(xml_file, csv_file)
