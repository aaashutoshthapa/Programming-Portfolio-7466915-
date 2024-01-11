# Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).

def get_num():
    number=int(input("Enter a number in decimal that you wish to convert: ")) # Prompts user to get input
    return number

def conversion(number):
    if number<0:  # Check if the number is less than zer
        print("Enter a positive intiger!!!")
    elif number == 0: # Check if the number is zero
        x = 0
        return x
    else:
        x= bin(number)[2:]  # Convert the number to its binary representation and remove the '0b' prefix
        return x

def get_display(x):
    print(f"The binary of {number} is {x}")
    pass

number=get_num()
y=conversion(number)
get_display(y)

    
