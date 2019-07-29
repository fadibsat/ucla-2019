s=-7
t=6
k=0
n=int(input('input n: '))
while k < n :
    s=1/3*(s+2*t)
    t=1/5*(s+4*t)
print(s,",",t)    
