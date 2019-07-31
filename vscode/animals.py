#Given a string containing a bunch of words
#separated by spaces, e.g.
# s = "bear dog cat bear bear tree bush cat tree bear"
#
# print each unique word in that string once, followed by
# the number of times it appeared, sorted so that the most
# frequent words are printed first
#
# Using the example string s above, you should get:
#   bear 4
#   cat 2
#   tree 2
#   dog 1
#   bush 1

s = "bear dog cat bear bear tree bush cat tree bear"
bear,a,b,c,d,e=0,0,0,0,0,0
cat=0
tree=0
dog=0
bush=0
for word in s.split(' '):
    word=a
    if a==word :
        bear+=1
    elif word!=a:
        b=word
        cat+=1
    elif word!=a and word!=b :
        c=word
        tree+=1            
    elif word!=a and word!=b and word!=c
        d=word
        dog+=1
    elif word!=a and word!=b and word!=c and word!=d :
        e=word
        bush+=1 
print("bear",bear)        
print("cat",cat)
print("tree",tree)
print("dog",dog)
print("bush",bush)
