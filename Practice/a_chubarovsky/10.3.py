import urllib.request
import lxml.html
connection = urllib.request.urlopen('http://google.com')

dom = lxml.html.fromstring(connection.read())

for link in dom.xpath('//a/@href'):
    print(link, f'Result code: {connection.getcode()}')
