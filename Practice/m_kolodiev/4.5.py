def rpl(string, dic):
    for i in string.split():
        if i in dic:
            string = string.replace(i, dic[i])
    return string


str1 = "Transactions are limited to a minimum of 100 USD or 80 EUR per transaction and maximum of 500 USD or 400 EUR."
lst1 = {'USD': 'dollars', 'EUR': 'euros'}
print(rpl(str1, lst1))
