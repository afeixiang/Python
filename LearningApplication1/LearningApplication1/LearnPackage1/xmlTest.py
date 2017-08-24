class xmlTest(object):
    """XML parsing and generating"""

    #import requests

def parse_html():
    """
    parse html function
    """
    import requests
    from lxml import html
    
    page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    buyers = tree.xpath('//div[@title="buyer-name"]/text()')
    #This will create a list of prices
    prices = tree.xpath('//span[@class="item-price"]/text()')
    print ('Buyers: ', buyers)
    print ('Prices: ', prices)

def parse_xml():
    """
    parse xml info and change the content
    """
    from bs4 import BeautifulSoup
    #open file tt.xml
    temp_xml_file = open('tt.xml','r')
    #read data
    xml_data = temp_xml_file.read()

    #into soup
    soup = BeautifulSoup(xml_data,'lxml')

    entitye_shapes = soup.find_all("entitytypeshape")
    for entity_s in entitye_shapes:
        entity_s['fillcolor'] = 'PPP'
        entity_s['width'] = '999'        
        print(entity_s.prettify)

    file2 = open('tt2.xml','w')
    file2.write(xml_data)
    file2.close
    #close file at the end
    temp_xml_file.close

def parse_xml2():
    """
    using ElementTree
    """
    from xml.etree.ElementTree import ElementTree
    tree = ElementTree()
    tree.parse("tt.xml")
    root = tree.getroot()

    for entity_s in root.iter('EntityTypeShape'):
        entity_s.set('Width','2.5')

    tree.write('output.xml')

if __name__ == '__main__':
    parse_xml2()
