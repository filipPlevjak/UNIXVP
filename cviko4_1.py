#vypocet kombinacneho cisla pomocou faktorialu

#vypocet kombinacneho cisla pomocou faktorialu

#vypocet kombinacneho cisla pomocou faktorialu

def fakt(n):
	f = 1
	if n == 0:
		return 1
	if n == 1:
		return 1
	if n > 1:
		for i in range(1, n+1):
			f*=i
		return f

def fkt(n):
	return reduce(lambda x,y: x*y, range(1,n+1))
		
def rfakt(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return n*rfakt(n-1)


def fkombi(n,k):
	return fakt(n)//(fakt(k)* fakt(n-k))

def rkombi(n,k):
	if k == 1 or k == n:
		return 1
	else:
		return rkombi(n-1, -1)+rkombi(n-1,k)



d={(0,0):1,(1,0):1,(1,1):1}

def mkombi(n,k):
	
	if (n,k) not in d:
		if k == 0 or k == n:
			d[n,k]=1
		else:
			d[n,k]=mkombi(n-1,k-1)+mkombi(n-1,k)
	return d[n,k]
		
	print (d)


 
	

