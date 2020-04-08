class MyClass:
    def __init__(self):
        self.a = 0
        self.b = 0

    def __add__(self, other):
        m = MyClass()
        m.a = self.a + other.a
        m.b = self.b + other.b
        return m

    def __str__(self):
        return f"MyClass: a = {self.a}, b = {self.b}"

    # неудобная и неочевидная реализация
    def AddMethod(self, another):
        m = MyClass()
        m.a = self.a + another.a
        m.b = self.b + another.b
        return m


x = MyClass()
x.a = 10
x.b = 20
y = MyClass()
y.a = 100
y.b = 200
z = MyClass()
s = MyClass()
s.a = 100
s.b = 200

print(x + y + z + s)
print(x.AddMethod(x.AddMethod(x.AddMethod(x.AddMethod(x.AddMethod(y))))))
