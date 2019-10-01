'''
The iterator for partition of loaded text from txt-file
with the specified delimiter.
Realization with the txt-file which is opened inside py-file.
PARAMETERS:
    delim - specified delimiter
NOTES:
    \n is the end of a line
    \t is Tab symbol
!!! There is a particular case of last partition, but I'll write it later.
'''

class MyIter:
    def __init__(self, text, delim):
        self.text = text
        self.delim = delim
        self.j1 = 0  # index of letter with which partition starts

    def __iter__(self):
        return self

# If j1 has self to be an instance atribute,
# i.e. self.j1 will be changed at every step of next procedure.
# In opposite case it will be local variable
# and at every next procedure should be initialised.
    def __next__(self):
        self.j2 = st.find(self.delim, self.j1)  # index of the end of partition
        # print(self.j2)

        if self.j1 == None:
            raise StopIteration
        elif self.j2 > 0:
            piece = st[self.j1:self.j2 + 1]
            self.j1 = self.j2 + 1
        else:
            piece = st[self.j1:]
            self.j1 = None
        return piece


with open('yellow_subm.txt','r') as fo:
    st = fo.read()
    # print('Length of text is ' + str(len(st)) + ' symbols.\n')

splitted = MyIter(st, '\n')

for pp in splitted:
    print('- - -')
    print(pp)