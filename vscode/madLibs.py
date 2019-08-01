def main():
    # The main function
    # When you run this program, it will execute the code in this function
    print("Mad libs program is running.")
    story = pickAStory()
    completed_story = fillInBlanks(story)
    print(completed_story)

def isAllCaps(text):
    # isAllCaps is to help fillInBlanks (defined farther down)
    # It should return True if all the letters in 'text' (function parameter) are capital letters
    # return false otherwise
    # The parameter 'text' will be a string

    allowed_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ',"'"]
    #----------------------
    # your code here
    #----------------------
    return False

def askForWord(type):
    # askForWord is to help fillInBlanks  (defined below)
    # The paramter 'type' will be a string of capital letters that corresponds to a blank in a story
    # Examles:
    #   "PLACE", "PERSON", "BODY PART"
    #
    # Print a message asking the player to enter this type of word
    # Return the player's input

    print("Choose a year")
    YEAR=input()
    print("Choose a place")
    place=input()
    print('choose a job')
    job=input()
    print('choose a continent')
    CONTINENT=input()
    
    return ""
    

def fillInBlanks(story):
    # fillInBlanks should search the story for blanks (words that need to be filled in by the players)
    # Blanks will be marked by asterisks (*) on both ends, and will say what type of thing to ask for in all caps
    # Example:
    #   "*HISTORICAL FIGURE* went to the *PLACE* to *ACTION VERB* some *TYPE OF FOOD*."
    #   The blanks are HISTORICAL FIGURE, PLACE, ACTION VERB, and TYPE OF FOOD
    # You can use isAllCaps() to help identify the blanks
    #
    # Use the askForWord() function to get the words the players want to fill in the blanks with
    #
    # Outline of the code:
    #   split the story up into a list to isolate the blanks
    #   replace the blanks with the words that players entered
    #   join the list back up into a finished story and return it

    text = story.split()   #figure out how best to split the story's text up (which character to use)
    #----------------------
    # your code here
    #----------------------
    return story

def pickAStory():
    #OPTIONAL
    # You can add your own stories here
    # And have pickAStory() return a random one

    stories = []
    stories.append("In *YEAR*, Napoleon Bonaparte invaded *PLACE* to fulfill his ambition of becoming *JOB* of all *CONTINENT*.")
    #----------------------
    # your code here
    #----------------------
    return stories[0]  #if you have multiple stories, need to modify this to return a random one, instead of always the 0th one

if __name__ == "__main__":
    main()
