print("Число кратное трём - Fizz."
      "\nЧисло кратное пяти - Buzz."
      "\nЧисло кратное пятнадцати - FizzBuzz."
      "\n")
for value in range(1, 101):
    if value % 15 == 0:
        print("FizzBuzz")
    elif value % 3 == 0:
        print("Fizz")
    elif value % 5 == 0:
        print("Buzz")
    else:
        print(value)
