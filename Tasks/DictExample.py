d = {}
while True:
   a = input('Input key :')  # String just to indicate the 'need to input'
   if a == "stop": # The pair with key 'stop' is also generated.
       # To avoid this, may be this if-condition should be after input?
       break
   if a not in d:  # Why for we check input key in the set of values?
       d[a] = 1
   else:
       d[a] += 1
   if a == "stop": # The pair with key 'stop' is also generated/
       # To avoid this, may be this if-condition should be after input?
       break

for i in d.items():
    print(i)