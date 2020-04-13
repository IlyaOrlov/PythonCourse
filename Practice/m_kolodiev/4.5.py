import re


def rpl(string, dic):
    pattern = re.compile('|'.join(dic.keys()))
    string = pattern.sub(lambda x: dic[x.group()], string)
    return string


str1 = "Transactions are limited to a minimum of 100 USD, or 80 EUR per transaction and maximum of 500 USD or 400 EUR"
lst1 = {'USD': 'DOLLARS', 'EUR': 'EUROS'}

print(rpl(str1, lst1))
