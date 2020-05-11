from urllib import request
import re

def collect_links(url):
    list_of_links = []
    req = request.Request(url)
    response = request.urlopen(req)
    web_page = response.read()
    print(web_page)
    search_res = re.findall(r'href="(http(s?)://.*?)"', str(web_page))
    for each in search_res:
        list_of_links.append(each)
    return list_of_links

print(collect_links('http://google.com'))