from bs4 import BeautifulSoup, SoupStrainer
import requests
from requests import HTTPError

url = 'https://www.google.com'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser', parse_only=SoupStrainer('a'))
urls = [link['href'] for link in soup if link.get('href')]

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(f'Success! {url}')







