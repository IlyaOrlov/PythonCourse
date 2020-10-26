from urllib import request
from bs4 import BeautifulSoup


def find_all_links(url):
    all_links = []
    req = request.Request(url)
    response = request.urlopen(req)
    web_page = response.read()
    soup = BeautifulSoup(web_page, "html.parser")
    for link in soup.find_all('a'):
        all_links.append(link.get('href'))
    return all_links


def check_links(links):
    w_link_counter = 0
    n_link_counter = 0
    for link in links:
        try:
            req = request.Request(link)
        except ValueError:
            n_link_counter += 1
            continue
        response = request.urlopen(req)
        if response.getcode() == 200:
            print('This is a working link {}'.format(link))
            w_link_counter += 1
        else:
            n_link_counter += 1
    print('There are {} working and {} nonworking links'.format(w_link_counter, n_link_counter))

check_links(find_all_links('http://google.com'))
