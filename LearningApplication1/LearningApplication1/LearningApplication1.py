import requests
from lxml import html

USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

LOGIN_URL = "https://www.school24.net.au/ps_parent_dologin.asp"

URL = "https://www.school24.net.au/ri/psn_oh.asp"
#URL = "https://www.school24.net.au/ri/ps.asp"
def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "username": "afeixiang@gmail.com", 
        "password": "woshiafei"
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("/html")

    print(tree.__str__)

if __name__ == '__main__':
    main()