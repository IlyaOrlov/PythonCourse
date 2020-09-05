import re

with open('myfile.txt') as f:
    for line in f:
        # netops.microsoft.com - - [01/Jul/1995:07:43:07 -0400] "GET /history/gemini/gemini.html HTTP/1.0" 200 2522
        # res = re.findall(r'\[(.*/.*/.*:\d{2}:\d{2}:\d{2}).*$', line)
        res = re.findall(r'\[(.{11}).*$', line)
        print(res)
