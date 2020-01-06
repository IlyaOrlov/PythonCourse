if __name__ == '__main__':
    dictionary = {'ll': 'LL', 'h': 'H', 'wo': 'WO', '!': '!!!'}

    string = "hello world!"
    print ('original string:{}'.format(string))
    for d in dictionary.keys():
        string = string.replace(d, dictionary[d])
    print ('edited string:{}'.format(string))