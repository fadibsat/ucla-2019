 ####################### PART ONE #########################
def max(a, b):
    # 1) create a program that checks which input/argument (a or b) is bigger
    if a>b:
        big=a
    elif b>a:
        big=b
    else :
        big=a        
    # 2) return the bigger value
    ################### YOUR CODE BELOW ######################


    return big
    ##########################################################

# Test Cases:
print('max() results below: ')
print(max( 2, 10))
print(max( 4, 4))
print(max( 33, 32))
print(max( -50, -5))
print(max( -1, 0))









####################### PART TWO #########################
# 1) create your own function called findMax
# 2) findMax will take a LIST as an input/argument
# 3) use the max function from Part One to find the maximum value in the LIST
# 4) return the max value
# hint: create an empty function first and
# hint: test that you can properly invoke/call the function in part 3

################### YOUR CODE BELOW ######################

def findMax(n):
    g=n[0]
    for i in n:
        g=max(i,g)
    return g


        
    


##########################################################









####################### PART THREE #########################
# 1) Run your findMax function using the Test Cases below as the inputs

# Test Cases:
list1 = [4,2,99,32,50]
list2 = ['mars', 'mark', 'marge', 'marvel', 'mares']
list3 = ['Narwhal', 'Chinese Water Deer', 'Pangolin', 'Bat-eared Fox','Markhor']
list4 = ['Daisy', 'iris', 'Violet', 'poppy', 'Lily']

##################### EXAMPLE ############################
# We created two functions below called firstFunction() and anotherFunction()
# anotherFunction() uses firstFunction() and then we printed the results
# Feel free to uncomment and run the program below:
#
# def firstFunction(a,b):
#     return [a,b]

# def anotherFunction (someList):
#     return(firstFunction(someList[1], someList[3]))

# print('anotherFunction() results below: ')
# aList = [1,2,3,4]
# b = anotherFunction(aList) 
# print(b)
#
##########################################################
print('findMax() results below: ')
################### YOUR CODE BELOW ######################
print(findMax(list1))
print(findMax(list2))
print(findMax(list3))
print(findMax(list4))




##########################################################



