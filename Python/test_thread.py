import threading

count = 0

def addone():
 	global count,lock
 	for i in range(100000):
 		#如果count+1的时候不加锁，多个线程同时作用于count上，会导致有的线程没加到
 		lock.acquire() 
 		count += 1
 		lock.release()

threads=[]

lock = threading.Lock() #创建锁
for i in range(5):
 	threads.append(threading.Thread(target=addone))

for j in threads:
 	j.start() #所有子线程执行
 	print(j.getName())

for k in threads:
 	k.join() #等待所有子线程执行完毕

print(count)	