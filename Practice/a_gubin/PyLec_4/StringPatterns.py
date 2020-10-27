def formatting(_string, patterns):
    for key, value in patterns.items():
        _string = _string.replace(key, value)
    return _string


string = '!some,text!,he,re!'
patterns = {'!': '?', ',': '|'}
print(formatting(string, patterns))
