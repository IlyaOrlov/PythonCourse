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

Realization with Python 3.6.
Last date: 2019 Oct 21
List of modifications:
1. Realization with single for-loop
    instead of previous version with 3 functions.
2. Arrangement within PEP8 desires.
"""


# action may be coding (action=integer)
# or decoding (action=integer, which is opposite to coding action)
def vigenere(text, coding_key_string, action):
    if action % 128 == 0:
        print('Please, choose an action in range [1 .. 127], '
              'otherwise your text will not be encrypted.')
        return None
    numlst_init = []
    text_encr = ''
    for k in range(len(text)):
        # Transform characters of text to the list of numbers
        # according ASCII table (128 symbols):
        numlst_init.append(int(ord(text[k])))
        # Displace symbols according to Vigenere mask:
        x = (numlst_init[k]
             + action
                 * ord(coding_key_string[k % len(coding_key_string)])) % 128
        # Transform list of numbers to the text
        # according ASCII table (128 symbols):
        text_encr += chr(x)
    return text_encr


### TEST
string1 = 'Climb Mount Niitaka'
key_str = 'Yamamoto'
action = 19
print('  == UNIVERSAL ==')
print('key string    : {}'.format(key_str))
print('multiplier = {}'.format(action))
print('plaintext     : {}'.format(string1))
string2 = vigenere(string1, key_str, action)
print('encrypted text: {}'.format(string2))
print('decrypted text: {}'.format(vigenere(string2, key_str, -action)))
