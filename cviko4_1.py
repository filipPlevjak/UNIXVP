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
		
def rfakt(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return n*rfakt(n-1)

