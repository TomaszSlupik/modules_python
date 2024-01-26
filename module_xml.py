import xml.etree.ElementTree as ET

# Otwarcie pliku xml
tree = ET.parse('books.xml')
root = tree.getroot()
print(ET.tostring(root, encoding='utf-8').decode('utf-8'))

print('---')

