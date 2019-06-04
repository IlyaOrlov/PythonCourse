i = 1
temp = ""
while i < 101:
   if i % 3 == 0 or i % 5 == 0:
       temp = ""
       if i % 3 == 0:
           temp="Fizz"
       if i % 5 == 0:
            temp = temp + "Buzz"
   else:
        temp = i
   print(temp)
   i+=1
print("END")