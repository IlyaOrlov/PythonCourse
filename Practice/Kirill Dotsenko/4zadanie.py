a="\tb\tgt\tb\t    r    e    r"
c=""
i=0
for b in a:
	if b=="\t":
		c+="    "
	elif b==" ":
		i+=1
	#elif b!=" ":
		#i=0
		#c+=b
	elif i==4:
		c+=r"\t"+b
		i=0
	elif b!="\t" and b!=" ":
		c+=b
print(c)
