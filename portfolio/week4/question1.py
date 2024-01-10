# Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.


# Define a validation function that checks if a number is between 0 and 100 (inclusive)
def validation(num):
    return 0 <= num <= 100

# Prompt the user to enter a number for validation
num = int(input("Enter a number that you wish to validate "))

# Display the entered number and whether it's valid based on the validation function
print(f"Number: {num}, Valid: {validation(num)}")



