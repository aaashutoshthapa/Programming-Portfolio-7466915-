# Write and test a function that takes a string as a parameter and returns a sorted list
# of all the unique letters used in the string. So, if the string is cheese, the list
# returned should be ['c', 'e', 'h', 's'].


def inps():
    word= input("Enter your word: ") #prompts user to enter value 
    return word
    
def unique_letters(word):
    result= sorted(list(set(word))) 
    return result

def oups(result):
    print ("The unique letters are : ", result)


word=inps()
result=unique_letters(word)
oups(result)
