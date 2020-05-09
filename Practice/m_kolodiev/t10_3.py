from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import re

website = urlopen("https://www.google.com/")

html = website.read().decode()
links = re.findall('"(https?://.*?)"', html)
for link in links:
    try:
        response = urlopen(link)
    except HTTPError as e:
        print(link + " The server couldn't fulfill the request. Error code: ", e.code)
    except URLError as e:
        print(link + " Failed to reach a server. ", e.reason)
    else:
        print(link + " The link is working fine")
