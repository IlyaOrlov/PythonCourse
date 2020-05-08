class Singleton:
    obj = None

    def __new__(cls):
        if cls.obj == None:
            cls.obj = super().__new__(cls)
        return cls.obj

s1 = Singleton()
s2 = Singleton()
assert(id(s1)==id(s2))  # True