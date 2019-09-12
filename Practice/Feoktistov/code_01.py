class comparision:

    def input(args):
        args.a= int(input('Введите первое значение для сравнения а='))
        args.b= int(input('Введите второе значение для сравнения b='))
        return args

    def compare(self, arg):

        if self.a > self.b:
            print('первое значение больше')
        elif self.a < self.b:
            print('второе значение больше')
        else:
            print('равные значения')

def Main():
    compar=comparision()
    compar.compare(compar.input())

Main() 