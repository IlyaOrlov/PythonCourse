class ReaderLine:

    def __init__(self, text, symbol):
        self.text, self.symbol, self._index_start = text, symbol, 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index_start < len(self.text):
            buf = []
            for i in range(self._index_start, len(self.text)):     # start with the new self._index_start
                if self.text[i] != self.symbol:
                    buf.append(self.text[i])
                    if i == len(self.text) - 1:                    # if this is the last symbol and
                        self._index_start = i + 1                  # our buf isn't empty
                        return "".join(buf)                        # for return string, because we work with list[]

                elif self.text[i] == self.symbol:
                    self._index_start = i + 1                     # new start index, go to the next symbol
                    return "".join(buf)                           # for return string, because we work with list[]

        raise StopIteration


if __name__ == "__main__":
    for line in ReaderLine("On Two\tThree\t...Seven", "\t"):
        print(line)
