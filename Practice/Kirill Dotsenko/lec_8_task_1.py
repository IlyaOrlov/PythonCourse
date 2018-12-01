import threading
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
chisla={10001:3,20000:10001,30000:20001}
start=time.time()
threads=[]
for k,v in chisla.items():
	thr=threading.Thread(target=find_primes,args=(k,v))
	thr.start()
	threads.append(thr)
for a in threads:
	thr.join()		
print('Общее время вычислений:{}'.format(int(time.time()-start)))
