import re
from urllib import request


def google_links(url):
    links = []
    req = request.Request(url)
    response = request.urlopen(req)
    web_page = response.read()
    search_res = re.findall(r'href="(http(s?)://.*?)"', str(web_page))

    for each in search_res:
        req_each = request.Request(each[0])
        response_each = request.urlopen(req_each)
        data = response_each.getcode()
        
        if data == 200:
            links.append(each[0])

    return links


if __name__ == '__main__':
    print(google_links('http://google.com'))
