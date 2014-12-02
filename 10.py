import math as mt
def isPrime(x):
    flag=1
    for i in range(2,int(mt.sqrt(x))+1):
        if x%i==0:
            flag=0
            break
    return flag
suma=0
for i in range(2,2000000,2):
    if isPrime(i):
        suma=suma+i
print(suma)        
