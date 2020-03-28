class Parent:
    num = 0

    def __new__(cls):
        cls.num += 1
        return super().__new__(cls)

    @classmethod
    def get_num_of_objects(cls):
        return cls.num

class Child(Parent):
    num = 0


p1 = Parent()
p2 = Parent()
c1 = Child()
print(Parent.get_num_of_objects())  # 2 Parent objects
print(Child.get_num_of_objects())   # 1 Child object
