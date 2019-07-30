#BEGINNING OF PRIME.PY
#work on this when you are done with other work
#
#implement this function, isPrime(n)
#which should return True if n is prime
#and False otherwise
#examples:
#   isPrime(1) returns False
#   isPrime(5) returns True
#   isPrime(28) returns False
#

def isPrime(n):
    i=1
    control=0
    n = str(n)
    if n[-1]==2 or n[-1]==0 or n[-1]==5 or n[-1]==4 or  n[-1]==6 or  n[-1]==8:
        return False
    n=int(n) 
    while i < n :
        if n%i==0 and i!=n and i!=1:
            control+=1
        if n==1 or n==0:
            control=100
        i+=1
    if control!=0:
        return False
    if control==0 :
        return True               

     
print(isPrime(19))  




#implement generatePrimes(n)
#which should return a list containing all the primes up to n
#Examples:
#   generatePrimes(1) should return []
#   generatePrimes(5) should return [2,3,5]
#   generatePrimes(20) should return [2,3,5,7,11,13,17,19]
def generatePrimes(n):
    prime=[]
    i=1
    for i in range(n):
        if isPrime(i):
            prime.append(i)
    return prime   
            
print(generatePrimes(10))  
#END OF PRIME.PY