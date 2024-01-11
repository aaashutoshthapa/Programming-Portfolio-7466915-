# Write and test a function that determines if a given integer is a prime number. A
# prime number is an integer greater than 1 that cannot be produced by multiplying
# two other integers.

def inp():
    while True:  # Initiates an infinite loop to handle user input until a valid integer is received
        try:
            num = int(input("Enter a number: "))  # Asks the user to input a number
            if num <= 1:  # Checks if the entered number is less than or equal to 1
                print("Number must be greater than 1")  # Prints a message prompting the user to enter a number greater than 1
            else:
                return num  # If the entered number is valid, returns the number and exits the loop
        except ValueError:  # Handles the ValueError if the input is not a valid integer
            print("Invalid input! Please enter an integer.")  # Prints a message for invalid input prompting the user to enter an integer


def is_prime(num):
    if num <= 1:  # Checks if the number is less than or equal to 1
        print("Number must be greater than 1")  # Prints a message prompting the user to enter a number greater than 1
        return False  # Returns False as numbers less than or equal to 1 are not prime
    
    # Checks for factors from 2 up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # Checks if the number is divisible by 'i' without a remainder
            print(f"The number {num} is not a prime number.")  # If divisible, prints that the number is not a prime number
            return False  # Returns False as the number is not prime
    
    print(f"The number {num} is a prime number.")  # Prints that the number is a prime number if no factors are found
    return True  # Returns True as the number is prime

num = inp()  # Calls the inp() function to get a number from the user
is_prime(num)  # Calls the is_prime() function to determine if the entered number is prime
