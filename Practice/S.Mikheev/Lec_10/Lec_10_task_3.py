from urllib import request
import re
from urllib.error import HTTPError


req = request.Request('http://google.com')
response = request.urlopen(req)
print("result code: {}".format(response.getcode()))
data = response.read()
results = re.findall(r'(https?://[^\s\";]+)', data.decode())
for link in results:
    try:
        url = request.urlopen(link)
        if url.getcode() == 200:
            print(link)
    except HTTPError as err:
        print('The link {}  does not open. Error: {}'.format(link, err))