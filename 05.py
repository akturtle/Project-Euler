import math as mt

def isPrime(x):
    flag=1
    for i in range(2,int(mt.sqrt(x))+1):
        if x%i==0:
            flag=0
            break
    return flag

x=21
list=[]
for i in range(2,x):
    if isPrime(i):
        k=i
        n=2
        while  i**n<x:
            k=i**n
            n=n+1
        list.append(k)
       # print(list)
product=1
for element in list:
   product=product*element
print(product)
