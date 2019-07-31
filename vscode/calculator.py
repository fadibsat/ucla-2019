#BEGINNING OF CALCULATOR


# 1) use if-statements to complete this calculator program with 4 operations
# Example run (what it should look like):
#       0 - add
#       1 - subract
#       2 - multiply
#       3 - divide
#   Enter a number to choose an operation:
#   1
#   Enter your first input: 10
#   Enter your second input: 4
#   10 - 4 = 6

# 2) add a fifth operation, power, that does a to the power of b
# 3) add a sixth operation, square root, that only asks for 1 input number and outputs its sqrt
# 4) seventh operation, factorial(a), one input
# 5) eighth operation, fibonacci(a), one input
# 6) talk to instructors when finished


print("  0 - add")
print("  1 - subract")
print("  2 - multiply")
print("  3 - divide")
print("  4 - power")
print("  5 - factorial")
print("  6 - square root")
print("Enter a number to choose an operation: \n")
op = int(input())

from math import *

    

a = int(input("Enter your first input: "))
if op<=4:
    b = int(input("Enter your second input: "))
    if op ==0:
        print(a,"+",b,"=",a+b)
    elif op ==1:
        print(a,"-",b,"=",a-b)
    elif op ==2:
        print(a,"x",b,"=",a*b)
    elif op ==3:
        print(a,"/",b,"=",a/b)  
    elif op==4:
        print(a,'to the power of ',b,'is',a**b)
else:
    if op==5:
        res=factorial(a)
        print(a,"factorial is" ,res)
    elif op==6:
        print('the square root of',a,'is',sqrt(a))
    elif op==7:
            





#END OF CALCULATOR