primos = []
def isprime(n):
    raiz=n**(1/2)
    for i in primos:
        if i > raiz + 1:
            primos.append(n)
            return True

        if n % i == 0 :
            return False

    primos.append(n)
    return True

def getprimes(value):
    p=2
    while len(primos)<value:
        isprime(p)
        p=p+1

getprimes(20000)
print(primos)
