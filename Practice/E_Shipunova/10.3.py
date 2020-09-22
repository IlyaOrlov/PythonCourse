from urllib import request
import re


def collect_working_links(url):
    list_of_links = []
    req = request.Request(url)
    response = request.urlopen(req)
    web_page = response.read()
    search_res = re.findall(r'href="(http(s?)://.*?)"', str(web_page))

    for each in search_res:
        req_of_each = request.Request(each[0])
        response_of_each = request.urlopen(req_of_each)
        code_of_link = response_of_each.getcode()

        if code_of_link == 200:   # if our link is working
            list_of_links.append(each[0])

    return list_of_links


if __name__ == '__main__':
    print(collect_working_links('http://google.com'))
