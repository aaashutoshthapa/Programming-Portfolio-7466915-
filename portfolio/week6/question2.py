# Write and test a function that takes an integer as its parameter and returns the
# factors of that integer. (A factor is an integer which can be multiplied by another to
# yield the original).

def get_value():
    num = int(input("Enter a number: ")) #prompts user to enter a number
    return num

def calc(num):
    factor=[] #creates a empty list
    for i in range(1, num + 1):  # Loop through numbers from 1 to 'num'
        if num % i == 0:  # Check if 'num' is divisible by 'i' without remainder
            factor.append(i)  # If divisible, 'i' is a factor of 'num', add it to the factors list
    return factor

def get_result():
    print(f"The factors of {num} are: {factor}")


num=get_value()
factor=calc(num)
get_result()
