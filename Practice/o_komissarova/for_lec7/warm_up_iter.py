class MyIter:
    def __init__(self, text, separator):
        self.text = text
        self.separator = separator
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        text_array = self.text.split(self.separator)
        if self.position < len(text_array):
            result = text_array[self.position]
            self.position += 1
            return result
        else:
            raise StopIteration


for i in MyIter('123\t456\t789\t', '\t'):
    print(i)
