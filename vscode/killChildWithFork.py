import time

dictionary={
    1: "kid's brain in chunks oozing out of his eye." , 
    2: 'kid suffocates.',
    3: "you can see the last meal you fed your child using that same fork.",
    4:"fork is stuck in there, son turns into a pile of good-for-nothing flesh."
}

def checkAlive(kid):
    if kid.alive:
        print("My kid is alive! Woo hoo! Good parenting!")
    else:
        print("... Woops, please clean up the pool of blood")

class Fork:
    child = None
    def killChild(self):
        if self.child != None:
            self.child.kill()

class Child:
    age = 12
    alive = True
    def kill(self):
        kill=input("Kill Child With Fork? y/n")
        if kill=='y':
            self.alive = False
            how=int(input("in the: 1-eye/2-throat/3-guts/4-forehead ?"))
            print(dictionary[how])   
            
        else:
            self.alive = True
f = Fork()
myKid = Child()
f.child = myKid


f.killChild()
checkAlive(myKid)
