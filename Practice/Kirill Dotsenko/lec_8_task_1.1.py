import multiprocessing
import time
def find_primes(end,start=3):
	spisok=[]
	for a in range(start,end+1):
		c=a//2
		d=[]
		for b in range(1,c+1):
			ost=a%b
			if ost==0:
				d.append(ost)
		if len(d)<2:
			spisok.append(a)
	print(spisok)

if __name__=='__main__':
	chisla={10001:3,20000:10001,30000:20001}
	start=time.time()
	pr=[]
	p1=multiprocessing.Process(target=find_primes,args=(10001,3))
	p2=multiprocessing.Process(target=find_primes,args=(20000,10001))
	p3=multiprocessing.Process(target=find_primes,args=(30000,20001))
	#for k,v in chisla.items():
		#pro=multiprocessing.Process(target=find_primes,args=(k,v))
		#pro.start()
	#for a in pr:
		#a.join()
	p1.start()
	p2.start()
	p3.start()
	p1.join()
	p2.join()
	p3.join()
	print('{0:3.2f} sec.'.format(time.time()-start))
	"""не понимаю немного как решить проблему с отсчетом времени.
	Если я запускаю цикл то не выдает нужного результата"""
