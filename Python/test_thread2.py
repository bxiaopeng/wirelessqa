import threading,time

def test(str,n):
	for i in range(n):
		print(str,i)
		time.sleep(1)

t = threading.Thread(target=test,args=('线程1',3))
t2 = threading.Thread(target=test,args=('线程2',3))
t.start()
t2.start()