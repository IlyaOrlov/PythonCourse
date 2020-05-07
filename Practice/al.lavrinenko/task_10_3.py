import urllib.request
import re

# from https://gist.github.com/uogbuji/705383
URL_PAT = r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)' \
          r'(?:[^\s()<>]|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()' \
          r'<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>' \
          r'?\xab\xbb\u201c\u201d\u2018\u2019]))'

html_code = (urllib.request.urlopen(input()).read()).decode()
for i in re.findall(URL_PAT, html_code):
    url = ''.join(i)
    if not url.startswith('http'):
        url = 'https://' + url
    print(url)
    try:
        if urllib.request.urlopen(url).getcode() == 200:
            print('working')
        else:
            print('not working')
    except (urllib.error.URLError, urllib.error.HTTPError):
        print('not working')
