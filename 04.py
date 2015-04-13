def isPali(x):
 flag=0
 i=1
 y=0
 n=x
 while n :
     num=n%10
     y=y*10+num
     n=n//10
 if y==x:
     flag=1

 return flag
result=0
for i in range(999,100,-1):
    for j in range(i,100,-1):
        x=i*j
        if  isPali(x) and x>result:
            result=x

print(result)
         
    
    
      
