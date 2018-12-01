from multiprocessing import Process,Lock

def obrabotka(lock,*args):
	with lock:
		i=''
		k=[]
		for a in args:
			if isinstance(a,int) or isinstance(a,float):
				print(sum(args))
				break
			elif isinstance(a,str):
				i+=a
			else:
				for b in a:
					k.append(b)
		if i.isdigit():
			print(i)
		if k!=[]:
			print(k)
		
	
if __name__=='__main__':
	lock=Lock()
	p1=Process(target=obrabotka,args=(lock,1,2,3,4,5,6))
	p2=Process(target=obrabotka,args=(lock,'1','2','3','4','5'))
	p3=Process(target=obrabotka,args=(lock,[1],[2],[3]))
	p1.start()
	p2.start()
	p3.start()
	p1.join()
	p2.join()
	p3.join()
