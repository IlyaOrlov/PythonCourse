from urllib import request
import re


def check_references_on(url):
    response = request.urlopen(url)
    body = response.read().decode()
    for href in re.finditer(r'href="[^"]*"', body):
        reference = re.match('href="(.*)"', href.group(0)).group(1)
        if not reference.startswith("http"):
            reference = url + reference
        print(f"{reference} / {request.urlopen(reference).status}")


if __name__ == '__main__':
    url = "http://google.com"
    check_references_on(url)
