b=2
a=1
m=0
while a<4000000:
    if a%2==0:
        m+=a
    a,b=b,a+b
    
 
print(m)
