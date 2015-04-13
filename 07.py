import math as mt

def isPrime(x):
    flag=1
    for i in range(2,int(mt.sqrt(x))+1):
        if x%i==0:
            flag=0
            break
    return flag

i=2
n=1
while n<10001 :
    i=i+1
    if isPrime(i):
        n=n+1

print(i)
