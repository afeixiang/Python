"""
Used for parse school24 website
"""
def main():
    """
        #main entrance for the app
    """
    import requests
    import json
    #from lxml import html
    #from lxml import etree
    from bs4 import BeautifulSoup
    import pprint
    import os

    #USERNAME = "<USERNAME>"
    #PASSWORD = "<PASSWORD>"
    print(os.getcwd())
    login_url = "https://www.school24.net.au/ps_parent_dologin.asp"

    content_url = "https://www.school24.net.au/ri/psn_oh.asp"

    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(login_url)

    try:
        result.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    #Read username and password info from ini.json into payload
    with open('ini.json') as json_data:
        payload = json.load(json_data)

    print('-----Username and password read OK.-----')


    # Perform login
    result = session_requests.post(
        login_url, data=payload, headers=dict(referer=login_url))

    if result:
        print('-----Login OK.-----')

    # get the latest 5 orders from content_url
    result = session_requests.get(content_url, headers=dict(referer=content_url))
    try:
        result.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    if result:
        print('-----Get Orderlist OK.-----')
    #parse to soup using beautiful soap
    soup = BeautifulSoup(result.content.decode("utf-8"), "lxml")
    #find the table that contains the list
    table = soup.find("table", class_="w3-table w3-bordered w3-striped")
    strs = '{'
    for order_itme in table.find_all('tr', recursive=False):
        col_name = ['   DeliveryDate', '   Amount', '    Student', '    OrderID']        
        for order_item_content in order_itme.find_all('td', limit=4, recursive=False):
            strs = strs + '' + col_name.pop() + ':' + order_item_content.get_text() + ','
        strs = strs.rstrip(',')
        strs = strs + '\n'
    strs = strs + '}'
    pprint.pprint(strs)
    #save to file
    with open("Output.txt", "w") as text_file:
        print(strs, file=text_file)

if __name__ == '__main__':
    main()
