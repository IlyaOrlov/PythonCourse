class NotValidInput(Exception):
    pass

def to_roman(data):
    # Ничего на ум не пришло
    calendar = {'1':'I', '2':'II', '3':'III', '4':'IV', '5':'V',
                '6':'VI', '7':'VII', '8':'VIII', '9':'IX', '10':'X'}
    if isinstance(data, int) and (0 < data <= 10):
        for i in calendar:
            if str(data) == i:
                res = calendar.get(i)
                return res
    else:
        raise NotValidInput()
try:
    to_roman(5)
except NotValidInput:
    print('Значение не удовлетворяет условиям')