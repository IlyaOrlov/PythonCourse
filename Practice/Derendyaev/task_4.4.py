str1 = "А\tб    в    г  д    ежз\tкл м  н    опр"
str2 = ""
buff = 0

for each in str1:
    if each != " ":
        buff = 0
        if each == "\t":
            each = "    "
        str2 += each
    else:
        buff += 1
        if buff == 4:
            str2 = str2[:-3] + "\t"
        else:
            str2 = str2 + each

print(str2)