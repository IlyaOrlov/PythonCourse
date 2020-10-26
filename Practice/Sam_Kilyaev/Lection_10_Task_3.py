from urllib import request
import re


def give_working_links(url):
    links = []
    my_request = request.Request(url)
    my_response = request.urlopen(my_request)
    page = my_response.read()
    search_result = re.findall(r'href="(http(s?)://.*?)"', str(page))
    for each in search_result:
        req_of_each = request.Request(each[0])
        response_of_each = request.urlopen(req_of_each)
        return_code = response_of_each.getcode()
        if return_code == 200:
            links.append(each[0])
    return links


if __name__ == '__main__':
    print(give_working_links('http://google.com'))
