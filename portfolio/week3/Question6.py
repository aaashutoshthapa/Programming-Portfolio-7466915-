# Write a program that displays the "Seven Times Table". That is, the result of
# multiplying 7 by every number from 0 to 12 inclusive. The output might start:
# 0 x 7 = 0
# 1 x 7 = 7
# 2 x 7 = 14

for i in range(13): # Loop through numbers 0 to 12 inclusive (13 total iterations)
    print(f"{i} * 7 = {i*7}")  # Print the multiplication table for the 7 times table