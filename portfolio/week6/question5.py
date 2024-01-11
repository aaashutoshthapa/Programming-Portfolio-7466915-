# Another way to hide a message is to include the letters that make it up within
# seemingly random text. The letters of the message might be every fifth character,
# for example. Write and test a function that does such encryption. It should
# randomly generate an interval (between 2 and 20), space the message out
# accordingly, and should fill the gaps with random letters. The function should
# return the encrypted message and the interval used.
# For example, if the message is "send cheese", the random interval is 2, and for
# clarity the random letters are not random:
# send cheese
# s e n d c h e e s e
# sxyexynxydxy cxyhxyexyexysxye

import random

def user_inp():
    message=input("Enter a message that you want to encrypt: ") #prompts user to enter a message
    return message

def encryption(message):
    interval = random.randint(2, 20) # getsany random value between 2 and 20 exclusively  
    encrypted = ""

    for i, char in enumerate(message):
        encrypted += char
        if (i + 1) % interval == 0:
            encrypted += random.choice('abcdefghijklmnopqrstuvwxyz')

    return encrypted, interval

def display(encrypted, interval):
    print("Original message:", message)
    print("Encrypted message:", encrypted)
    print("Interval used:", interval)

message = user_inp()
encrypted, interval=encryption(message)
y=display(encrypted, interval)
