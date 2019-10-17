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
    < ; <=
    == ; !=
    >= ; >
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

### ARITHMETIC

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
            res = int(100 * res) / 100  # rounding to zero (negative float too)
            res_rub, res_kop = str(res).split('.')
            return Money(res_rub, res_kop)
        except TypeError:
            print('\nCheck the types of your variables: \n'
                  'first should be instance of class Money,\n'
                  'second should be a number (integer or float).\n'
                  'But you input {} and {}.\n'
                  .format(str(type(self)), str(type(other))))
            return None
            # raise TypeError


    def __truediv__(self, other):
        try:
            res = self.amount/other
            # print('\nresult of division is {}'.format(res))  ##
            res = int(100 * res) / 100  # rounding to zero (negative float too)
            res_rub, res_kop = str(res).split('.')
            # res_kop = res_kop[0:2]  # rounding toward zero (negative float too)
            # print('rounded value of cents is {}'.format(res_kop))  ##
            return Money(res_rub, res_kop)
        except TypeError:
            print('\nCheck the types of your variables: \n'
                  'first should be instance of class Money,\n'
                  'second should be a number (integer or float).\n'
                  'But you input {} and {}.\n'
                  .format(str(type(self)), str(type(other))))
            # return None
        except ZeroDivisionError:
            print('\nDescent people do not divide on 0!\n')
            # return None
        except Exception as ex:
            print('Something goes wrong with this division...\n{}'.format(ex))
        return None


### COMPARISON

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount


### CURRENCY CONVERSION
    @property
    def curr_exchange(self):
        return self.curr_exchange  # self._curr_exchange
    # As I understood we need @property
    # for creation a calculated property (attribute).
    # While @setter set the certain instruction (rule)
    # of calculation of this property.

## Variant 1 (old):
# 1. using 'setter' as a function
# 2. _curr_exchange was a protected attribute
    # @property
    # def curr_exchange(self):
    #     return self._curr_exchange

    # @curr_exchange.setter
    # def curr_exchange(self, currency):
    #     cec = dict(USD = 64.42, GBP = 79.19)  # hidden data
    #     x = self.amount/cec[currency]
    #     self._curr_exchange  = int(100*x)/100

## Variant 2 (new): curr_exchange is just a method of class
    def curr_exchange(self, currency):
        cec = dict(USD = 64.42, GBP = 79.19)  # hidden data
        x = self.amount/cec[currency]
        return int(100*x)/100


### TESTING
m1 = Money(200, 80)
m2 = Money(100, 64)
print(m1.amount)
print(m2.amount)

print('\n <<< ARITHMETIC >>>')
m3 = m1 + m2
print('\n')
print(' {}'.format(m1.amount))
print('+{}'.format(m2.amount))
print('=' * (len(str(m3.amount)) + 1) + ' Addition')
print(m3.amount)

m3 = m1 - m2
print('\n')
print(' {}'.format(m1.amount))
print('-{}'.format(m2.amount))
print('=' * len(str(m3.amount)) + ' Subtraction')
print(m3.amount)

multiplier = -3.1415926
m4 = m2*multiplier
print('')
print('{} * {}'.format(m2.amount, multiplier))
print('='*len(str(m2.amount)) + ' Multiplication')
print(m4.amount)

denominator = 3.25
m4 = m2/denominator
print('')
print('{} / {}'.format(m2.amount, denominator))
print('='*len(str(m2.amount)) + ' Division')
# print(m4)
print(m4.amount)

print('\n <<< COMPARISON >>>')
print('')
print('{} < {}'.format(m1.amount, m2.amount))
print(m1 < m2)

print('')
print('{} <= {}'.format(m1.amount, m2.amount))
print(m1 <= m2)

print('')
print('{} == {}'.format(m1.amount, m2.amount))
print(m1 == m2)

print('')
print('{} != {}'.format(m1.amount, m2.amount))
print(m1 != m2)

print('')
print('{} >= {}'.format(m1.amount, m2.amount))
print(m1 >= m2)

print('')
print('{} > {}'.format(m1.amount, m2.amount))
print(m1 > m2)


print('\n <<< CURRENCY CONVERSION >>>')

### Variant 1
# print('')
# key = 'USD'  # or 'GBP'
# m1.curr_exchange = key
# print('conversion sum {} in {}'.format(m1.amount, key))
# print(m1.curr_exchange)

### Variant 2
print('')
key = 'USD'  # or 'GBP'
print('conversion sum {} in {}'.format(m1.amount, key))
print(m1.curr_exchange(key))

# ### OFFTOPIC TEST for Anton
# Mlist = [m1, m2, Money(160, 84)]
# print('\n--- OFFTOPIC TEST for Anton [instance]')
# print(Money(200, 80) in Mlist)
# Mlist.append(m3)
# for x in Mlist:
#     if Money(200, 80) == x:
#         print('\nBingo!')
