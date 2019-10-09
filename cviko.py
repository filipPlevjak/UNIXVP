#project euler problemy: 2,25,7,10

fibo = [0,1]


def rfib(n)
	if n == 0
		fibo[0] = 0
	else if n == 1
		fibo[1] = 1
	else: 
		return rfib(n-1) + rfib(n-2)
		
		
		
fobi= {0: 0, 1: 1}


def mfobi(n):
	if n not in fobi:
		fobi[n] = mfobi(n-1) + mfobi(n-2)
	return fobi[n]

	
