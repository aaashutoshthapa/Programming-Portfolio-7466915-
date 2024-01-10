# Modify the "Times Table" again so that the user still enters the number of the table,
# but if this number is negative the table is printed backwards. So entering "-7"
# would produce the Seven Times Table starting at "12 times" down to "0 times"




# Prompt the user to enter a value for the multiplication table
x = int(input("Enter a value for a table you want to find: "))

# Check if the entered value is within the range of -12 to 12
if -12 <= x <= 12:
    if x >= 0:
        # If the value is non-negative, generate the multiplication table for that number (0 to 12)
        for i in range(13):
            print(f"{i} * {x} = {i * x}")
    else:
        # If the value is negative, generate the multiplication table in reverse (12 to 0) for its absolute value
        for i in range(12, -1, -1):
            print(f"{i} * {-x} = {i * (-x)}")
else:
    # If the input is outside the valid range, print an error message
    print("Invalid input!!!!")
