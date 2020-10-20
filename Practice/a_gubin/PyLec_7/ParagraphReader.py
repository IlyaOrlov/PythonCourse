import sys
import re


class ParagraphReader:
    def __init__(self, text, paragraph_sign="@"):
        self._re_iter = re.finditer(f"[^{paragraph_sign}]+", text)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._re_iter)[0]


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
