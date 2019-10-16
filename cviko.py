#project euler problemy: 2,25,7,10
#projecteuler.net/archives
fibo = [0,1]

def fib(n):
	a,b=0,1
	if n>1:
		for i in range(n-1):
			a,b,a+b
	return b

def rfib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else: 
		return rfib(n-1)+rfib(n-2)
		
		
fobi= {0: 0, 1: 1}


def mfobi(n):
	if n not in fobi:
		fobi[n] = mfobi(n-1) + mfobi(n-2)
	return fobi[n]

def mfib(n):
	if n>len(z)-1:
		z.append(mfib(n-1)+mfib(n-2))
		return z[n]
