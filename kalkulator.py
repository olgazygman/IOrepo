import math



liczby = input()

def newton(a):

    a = a.split()

    n = math.factorial(int(a[0]))

    k = math.factorial(int(a[1]))

    nk = math.factorial( int(a[0])-int(a[1]))

    N = n/(k*nk)

    return int(N)



def suma(a):

    a = a.split()

    x = math.factorial(int(a[0]))

    y = math.factorial(int(a[1]))

    sumaxy = x + y

    return int(sumaxy)



print(newton(liczby))

print(suma(liczby))

