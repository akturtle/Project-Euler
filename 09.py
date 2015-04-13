import math as mt

for c in range(420,998):
    x=mt.sqrt(2*c**2-(1000-c)**2)
    if int(x)**2==x**2 :
        print(x)
        a=(1000-c+x)/2
        b=(1000-c-x)/2
        print(b,c)
        if int(a)==a and int(b)==b :
            result=a*b*c
            break
    
print (result)    
