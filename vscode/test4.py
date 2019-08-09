a2DList = [[89,      10,     63],
            ["bird","is","word"],
            [0,       0,     1,]]

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def replaceNegatives(a2DList):
    #loop through a2DList and replace all negative numbers 
    # with the word "Nope"
    
    #----------------------
    i=int(a2DList[0][0]) 
    for i in a2DList:
        if i<0 and i==int:
            x=index_2d(a2DList,i)
            x=str(x)
            print(x)
            '''x.split(,)
            print(x)'''

            a2DList.replace('Nope')
    #----------------------
    
    #at the end, we print out the result
    print(a2DList)

replaceNegatives(a2DList)