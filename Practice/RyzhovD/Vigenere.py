"""
Here it is my realization of coder-decoder
    based on Chiffre de Vigenere
    (for details see https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).
Slight modification is as follows:
        encryption: E[i] = P[i] + A * K[i]  mod 128
        decryption: P[i] = E[i] - A * K[i]  mod 128
    Here E is encrypted text, P is plaintext, K is the key string (text).
    A is integer multiplier, which is equal to 1 for original Vigenere cipher.
    The multiplier A may be equal to any integer,
    but I use A in range [1 .. 127] mod 128. It is enough.

INPUT arguments are: string (text/data), key string, and an integer.
    Integer should be not multiple to 128 or equal to 0,
    otherwise text will not be encrypted.
OUTPUT is a text (string).
"""

# Transform characters of text to the list of numbers
# according ASCII table (128 symbols)
def str_to_numlist(str):
    numlst = []
    for x in str:
        numlst.append(int(ord(x)))
    return(numlst)


# Transform list of numbers to the text
# according ASCII table (128 symbols)
def numlst_to_str(numlst):
    str = ''
    for x in numlst:
        str = str + chr(x)
    return(str)


# action may be coding (action=integer)
# or decoding (action=integer, which is opposite to coding action)
def Vigenere(text, coding_key_string, action):
    if action%128 == 0:
        print('Please, choose an action in range [1 .. 127], '
              'otherwise your text will not be encrypted.')
        return (None)
    numlst_encr = []
    numlst_init = str_to_numlist(text)
    for k in range(len(numlst_init)):
        numlst_encr.append((ord(text[k])
                            + action*ord(key_str[k % len(key_str)]))%128)
    text_encr = numlst_to_str(numlst_encr)
    return(text_encr)



### TEST
str1 = 'Climb Mount Niitaka'
key_str = 'Yamamoto'
action = 3
print('  == UNIVERSAL ==')
print('key string    : {}'.format(key_str))
print('miltiplayer = {}'.format(action))
print('plaintext     : {}'.format(str1))
str2 = Vigenere(str1, key_str, action)
print('encrypted text: {}'.format(str2))
print('decrypted text: {}'.format(Vigenere(str2, key_str, -action)))
# print('---')
# print(str_to_numlist(str1))
# print(str_to_numlist(str2))
# print(str_to_numlist(Vigenere(str2, key_str, -action)))