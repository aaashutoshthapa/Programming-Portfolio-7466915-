# Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program




# Define a function 'count' that counts the number of uppercase and lowercase letters in a given string
def count(string):
    upper_case = 0  # Initialize the count for uppercase letters
    lower_case = 0  # Initialize the count for lowercase letters
    
    # Iterate through each character in the input string
    for char in string:
        # Check if the character is an uppercase letter and increment the count if true
        if char.isupper():
            upper_case += 1
        # Check if the character is a lowercase letter and increment the count if true
        elif char.islower():
            lower_case += 1
    
    # Return the counts of uppercase and lowercase letters
    return upper_case, lower_case


# Prompt the user to enter a string
string = input("Enter any string: ")

# Call the 'count' function to count the number of uppercase and lowercase letters in the entered string
upper_case, lower_case = count(string)

# Display the counts of uppercase and lowercase letters in the entered string
print(f"Uppercase letter count: {upper_case}")
print(f"Lowercase letter count: {lower_case}")

        