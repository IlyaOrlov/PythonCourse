'''
Operations with financial data.
Class Money is introduced as a set of 2 integers:
roubles and kopeks (or pounds and pennies).
Only decimal system is supported
(where the second unit is 1/100 of the first one,
e.g. old penny which is 1/240 of GBP do not satisfied to the class.)

There are three types of operations are defined:
1. arithmetic (rounding to zero (negative float too))
    addition
    subtraction
    multiplication
    true division
2.comparison (now only <)
    <
    # <=
    # ==
    # !=
    # >=
    # >
3. currency conversion

'''

class Money:
    def __init__(self, rub, kop):
        # Here should be checks for: rub and kop are integers; 0 <= kop < 100
        self.rub = rub
        self.kop = kop


    @property
    def amount(self):
        return float('{}.{}'.format(self.rub, self.kop))


    def __add__(self, other):
        res = self.amount + other.amount
        res = int(100*res)/100  # see, comment of subtraction
        res_rub, res_kop = str(res).split('.')
        return Money(res_rub, res_kop)


    def __sub__(self, other):
        res = self.amount - other.amount
        # print(res)  ##
        res = int(100*res)/100  # to exclude rounding errors,
                    # e.g., 200.80 - 100.64 = 100.16000000000001
        # print(res)  ##
        res_rub, res_kop = str(res).split('.')
        return Money(res_rub, res_kop)


    def __mul__(self, other):
        try:
            res = self.amount*other
            # print('\nresult of multiplicaion is {}'.format(res))  ##
        except:
            print('Check the types of your variables: \n'
                  'first should be instance of class Money,\n'
                  'second should be a number (integer or float).')
            raise TypeError
        res = int(100*res)/100  # rounding to zero (negative float too)
        res_rub, res_kop = str(res).split('.')
        return Money(res_rub, res_kop)


    def __truediv__(self, other):
        try:
            res = self.amount/other
            # print('\nresult of division is {}'.format(res))  ##
        except:
            print('Check the types of your variables: \n'
                  'first should be instance of class Money,\n'
                  'second should be a number (integer or float).')
            raise TypeError
        res = int(100*res)/100  # rounding to zero (negative float too)
        res_rub, res_kop = str(res).split('.')
        # res_kop = res_kop[0:2]  # rounding toward zero (negative float too)
        # print('rounded value of cents is {}'.format(res_kop))  ##
        return Money(res_rub, res_kop)


    def __lt__(self, other):
        if self.amount <= other.amount:
            return True
        else:
            return False

### CURRENCY CONVERSION
    @property
    def curr_exchange(self):
        return self._curr_exchange

    @curr_exchange.setter
    def curr_exchange(self, currency):
        cec = dict(USD = 64.42, GBP = 79.19)  # hidden data
        x = self.amount/cec[currency]
        self._curr_exchange  = int(100*x)/100

### TESTING
m1 = Money(200, 80)
m2 = Money(100, 64)
print(m1.amount)
print(m2.amount)

m3 = m1 + m2
print('\n')
print(' {}'.format(m1.amount))
print('+{}'.format(m2.amount))
print('='*(len(str(m3.amount)) + 1) + ' Addition')
print(m3.amount)

m3 = m1 - m2
print('\n')
print(' {}'.format(m1.amount))
print('-{}'.format(m2.amount))
print('='*len(str(m3.amount)) + ' Subtraction')
print(m3.amount)

multiplier = -3.1415926
m4 = m2*multiplier
print('')
print('{} * {}'.format(m2.amount, multiplier))
print('='*len(str(m2.amount)) + ' Multiplication')
print(m4.amount)

denominator = 7
m4 = m2/denominator
print('')
print('{} / {}'.format(m2.amount, denominator))
print('='*len(str(m2.amount)) + ' Division')
print(m4.amount)

print('')
print('{} < {}'.format(m1.amount, m2.amount))
print(m1 < m2)

print('')
key = 'USD'  # or 'GBP'
m1.curr_exchange = key
print('conversion sum {} in {}'.format(m1.amount, key))
print(m1.curr_exchange)