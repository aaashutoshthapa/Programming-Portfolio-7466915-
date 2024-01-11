# Computers are commonly used in encryption. A very simple form of encryption
# (more accurately "obfuscation") would be to remove the spaces from a message
# and reverse the resulting string. Write, and test, a function that takes a string
# containing a message and "encrypts" it in this way

def user_inp():
    message=input("enter the message that you wish to encript:")  #prompts the user to enter message
    return message

def encryption(message):
    # Remove spaces from the message by replacing them with an empty string
    message_without_spaces = message.replace(" ", "")
    
    # Reverse the message without spaces using slicing [::-1]
    encrypted_message = message_without_spaces[::-1]
    return encrypted_message

def encripted_message(encrypted_message):
    print("Original message:", message)
    print("Encrypted message:", encrypted_message)    

message = user_inp()
encrypted_message = encryption(message)
y=encripted_message(encrypted_message)

