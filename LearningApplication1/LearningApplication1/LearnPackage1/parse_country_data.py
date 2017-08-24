"""
For learning operate XML file through python ElementTree.
"""

def main():
    """
        #main entrance for the app
    """
    import xml.etree.ElementTree as ET
    tree = ET.parse('country_data.xml')
    root = tree.getroot()
    print(root.tag)
    print(root.attrib)
    print('----------------------')
    for child in root:
        print(child.tag)
        print(child.attrib)
    print('----------------------')
    for neighbor in root.iter('neighbor'):
        print(neighbor.attrib)
    print('----------------------')

#Element.findall() finds only elements with a tag which are direct children of the current element.
#Element.find() finds the first child with a particular tag,
#and Element.text accesses the element’s text content.
#Element.get() accesses the element’s attributes:

    for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get('name')
        print(name + '  '+ rank)




if __name__ == '__main__':
    main()
