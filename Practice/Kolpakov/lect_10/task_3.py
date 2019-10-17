from urllib import request
import re


req = request.Request('http://google.com')
response = request.urlopen(req)
web_page = (response.read()).decode()
#print(web_page)
urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', web_page)
print(urls)
print(len(urls))
for ur in urls:
    test = request.urlopen(ur)
    if test.getcode() == 200:
        print(ur)