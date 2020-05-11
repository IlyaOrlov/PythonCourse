d = {}
while True:
   a = input()
   if a not in d:
       d[a] = 1
   else:
       d[a] += 1
   if a == "stop":
       break

for i in d.items():
    print(i)