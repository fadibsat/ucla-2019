# Write a script that asks for an amount of change
# (as in money you get back when paying for something in cash)
# Then tells you how many of each type of coin to use to make that amount
#   Example:
#       How much change do you need?
#       83
#       3 quarters, 0 dimes, 1 nickel, 3 pennies


changeAmount =int( input("How much change do you need?\n"))
quarters = 0    #0.25
dimes = 0       #0.10
nickels = 0     #0.05
pennies = 0     #0.01
'''
if changeAmount>=25:
    while changeAmount>25:
        changeAmount-=25
        quarters+=1

if changeAmount>=10:
    while changeAmount>10:
        changeAmount-=10
        dimes+=1
if changeAmount>=5:
    while changeAmount>5:
        changeAmount-=5
        nickels+=1

if not changeAmount==0:
    while changeAmount!=0:
        changeAmount-=1
        pennies+=1   
'''
g=0
a=[25,10,5,1]   #change:3
b = [0,0,0,0]  # 3,0,1,0
for i in a:
    if i==1:
        b[3]=changeAmount
        
            
        # while changeAmount!=0:
        #     changeAmount-=1
        #     b[3]=+1
    while (changeAmount>=i and i!=1):
        changeAmount-=i
        b[g]+=1
    g+=1        
    
for i in range (4):
    # print(a[i])
    print(b[i])


print(b)
'''
print(83-25)
     
print(quarters,"quarters,",dimes,"dimes,",nickels,"nickels,",pennies,"pennies")
'''
