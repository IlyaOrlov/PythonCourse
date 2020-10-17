import sys


class ParagraphReader:
    def __init__(self, text, paragraph_sign="@"):
        self._text = text.split(paragraph_sign)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._text):
            paragraph, self._index = self._text[self._index], self._index + 1
            return paragraph
        raise StopIteration


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        text = ''
        try:
            with open(sys.argv[1], "rt") as file:
                text = file.read()
            reader = ParagraphReader(text, sys.argv[2])
            for paragraph in reader:
                print(paragraph)
        except OSError:
            print(f"The file '{sys.argv[1]}' opening failed")
    else:
        print(f"Need 2 parameters (the file name and the paragraph sign), but {len(sys.argv) - 1} given")
