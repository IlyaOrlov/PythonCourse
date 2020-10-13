class MyIter:
    def __init__(self, text, separator):
        self.text = text
        self.separator = separator
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        text_array = self.text
        result = ""
        while True:
            if self.position == len(text_array):
                raise StopIteration
            elif text_array[self.position] == self.separator:
                self.position += 1
            elif text_array[self.position + 1] == self.separator:
                result += text_array[self.position]
                self.position += 1
                return result
            else:
                result += text_array[self.position]
                self.position += 1


for i in MyIter('123\t456\t789\t', '\t'):
    print(i)
