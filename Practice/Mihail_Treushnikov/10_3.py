import re
from urllib import request


def get_working_urls(url):
    working_list = []
    req = request.Request(url)
    response = request.urlopen(req)
    web_page = response.read()
    links = re.findall('"((http|ftp)s?://.*?)"', str(web_page))
    for i in links:
        req_of_each = request.Request(i[0])
        response_of_each = request.urlopen(req_of_each)
        code_of_link = response_of_each.getcode()

        if code_of_link == 200:
            working_list.append(i[0])
    print(working_list)


if __name__ == '__main__':
    get_working_urls('http://google.com')
