# 06.11 - [ИО]:  Проверено (OK, но можно проще, используя метод строки replace).
stroka1 = ("the bus	arrived")
print(stroka1)
spisok = list(stroka1)
print (spisok)
i=0
for each in spisok:
	if spisok[i]=="\t":	     
	    spisok[i]="    "
	i +=1
stroka2="".join(spisok)
print (stroka2)
print (spisok)
j=0
for each in spisok:
	if spisok[j]=="    ": 
	    spisok[j]="\t"
	j +=1
stroka3="".join(spisok)
print (stroka3)
print (spisok)
