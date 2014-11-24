import math as mt

def isPrime(x):
    flag=1
    for i in range(2,int(mt.sqrt(x))):
        if x%i==0:
            flag=0
            break
    return flag

num=600851475143
k=0
for i in range(int(mt.sqrt(num)),2,-1):
    if num%i==0:
        if isPrime(i):
            k=i
            break
    
    
