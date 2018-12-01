import os
def cpdir(src,dst):
	try:
		os.mkdir(dst)
	except FileExistsError:
		print("Problemki")
	for file in os.listdir(src):
		if os.path.isfile(src + '/' + file):
			cpfile(src + '/' + file, dst + '/' + file)
		else:
			os.mkdir(dst + '/' + file)
			
	
cpdir('test','test2')
"""Думал как можно сделать лучше.Но я не знаю как применять os.walk()"""
