# When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)

def remove_last_chharacter(string):
    """Returns given string without its last character if there are more than 1"""
    if len(string)>1:  # Check if the length of the string is greater than 1
        return string[:-1]  # Return the string without its last character using slicing
    else:
        return string   # Return the original string if its length is 1 or less
    
string=input("enter a word or couple of words:")  # Prompt the user to enter a string
remove_last_chharacter(string)   

print(f'The output after removing the last character is: {remove_last_chharacter(string)}')

    

