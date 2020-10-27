class Human:

   def __init__(self, first_name, last_name, age, position, phone):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.position = position
       self.phone = phone

   def __iter__(self):
       return iter(self)
