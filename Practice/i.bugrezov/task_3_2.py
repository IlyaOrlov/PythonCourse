mydict = {"Barcelona":"FCB", "Real":"FCR", "Bavaria":"FCB"}
article = ("Barcelona won Real and lost Bavaria")
for key, val in mydict.items():
	article = article.replace(key, val)
print(article)
