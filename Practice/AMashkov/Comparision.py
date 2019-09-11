class comparision:

    def input(args):
        args.a= int(input('Введите первое число а='))
        args.b= int(input('Введите второе число b='))
        return args

    def compare(self, arg):

        if self.a > self.b:
            print('первое число больше')
        elif self.a < self.b:
            print('второе число больше')
        else:
            print('числа равны')

def Main():
    compar=comparision()
    compar.compare(compar.input())

Main()