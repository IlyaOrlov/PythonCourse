import re
from urllib import request


def get_urls(url):
    req = request.Request(url)
    response = request.urlopen(req)
    web_page = response.read()
    links = re.findall('"((http|ftp)s?://.*?)"', web_page)
    for link in links:
        print('link {} : {}'.format(link, url_ok(link)))


def url_ok(url):
    r = request.urlopen('http://google.com').getcode()
    return r.status_code == 200


if __name__ == '__main__':
    get_urls('http://google.com')
