a=input("Which string:").lower()
b=input("Which word do u want to replace:").lower()
c=input("On what:").lower()
d={'k':c}
for v in d.values():
	print(a.replace(b,v).title())
