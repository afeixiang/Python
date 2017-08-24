"""
For learning update edmx file through python ElementTree.
"""
def main():
    """
        #main entrance for the app
    """
    import xml.etree.ElementTree as ET
    tree = ET.parse('tt2.xml')
    root = tree.getroot()
    print(root.tag)
    print(root.attrib)
    ns_edmx = {'edmx': 'http://schemas.microsoft.com/ado/2009/11/edmx'}
    print('--------iter begin--------------')
    for entity_type_shape in root.iter('{http://schemas.microsoft.com/ado/2009/11/edmx}EntityTypeShape'):
        print(entity_type_shape.get('EntityType'))
        entity_type_shape.set('IsExpanded','true')
    tree.write('tt3.xml')
    print('----------iter end------------')
    entity_type_shape = root.find('edmx:Diagrams:EntityTypeShape', ns_edmx)
    #entity_type_shape.tag
    print(entity_type_shape.tag)

if __name__ == '__main__':
    main()
