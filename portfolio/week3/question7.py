# Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive



# Prompt the user to enter a value for the multiplication table
x = int(input("Enter a value for a table you want to find: "))

# Check if the entered value is within the range of 0 to 12
if 0 <= x <= 12:
    # Loop through numbers 0 to 12 inclusive (13 total iterations)
    for i in range(13):
        # Print the multiplication table for the user-provided value
        print(f"{i} * {x} = {i * x}")
else:
    # If the input is outside the valid range, print an error message
    print("Invalid input!!!!")
