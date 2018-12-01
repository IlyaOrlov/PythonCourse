def cpfile(src,dst):
	try:
		with open(src,'r') as f:
			contents=f.readlines()
		mes=''
		for a in contents:
			mes+=a
		with open(dst,'x') as f_obj:
			f_obj.write(mes)
	except Exception as exc:
		print("U tebya problema priyatel:{}".format(exc))
c=cpfile('kek.txt','kek2.txt')
