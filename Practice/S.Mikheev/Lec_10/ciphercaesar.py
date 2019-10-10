def decoder(phrase, step):
    step = -step
    with open('alphabet.txt', 'r') as f:
        alphabet = f.read()
    decod_phrase = ''
    for symbol in phrase:
        index = alphabet.find(symbol)
        new_index = step + index
        if step >= 0:
            while new_index >= len(alphabet):
                new_index -= len(alphabet)
            if new_index < len(alphabet):
                decod_phrase += alphabet[new_index]
        else:
            while new_index < -len(alphabet):
                new_index += len(alphabet)
            if new_index > -len(alphabet):
                decod_phrase += alphabet[new_index]
    return decod_phrase


def encoder(phrase, step):  # Буду использовать для шифровки сообщений "Шифр Цезаря"
    with open('alphabet.txt', 'r') as f:
        alphabet = f.read()
    phrase = phrase.strip(' ')
    encod_phrase = ''
    for symbol in phrase:
        index = alphabet.find(symbol)
        new_index = step + index
        if step >= 0:
            while new_index >= len(alphabet):
                new_index -= len(alphabet)
            if new_index < len(alphabet):
                encod_phrase += alphabet[new_index]
        else:
            while new_index < -len(alphabet):
                new_index += len(alphabet)
            if new_index > -len(alphabet):
                encod_phrase += alphabet[new_index]
    return encod_phrase
