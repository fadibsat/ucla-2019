import random
a=[]
i=0
b=0
for i in range(10):
    x=random.randint(0,30)
    a.append(x)
    b+=x
print(a,"the sum is ",b)
