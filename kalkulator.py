import math

a = input()
def newton(a):
	a = a.split()
	n = math.factorial(int(a[0]))
	k = math.factorial(int(a[1]))
	nk = math.factorial( int(a[0])-int(a[1]) )
	N = n/(k*nk)
	return int(N)

print(newton(a))


