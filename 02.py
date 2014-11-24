a=1
b=2
sum=2

while 1:
    c=a+b
    a=b
    b=c
    if c >4000000 :
        break
    if c%2==0:
        sum=sum+c
print(sum)
