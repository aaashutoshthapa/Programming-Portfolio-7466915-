# One approach to analysing some encrypted data where a substitution is suspected
# is frequency analysis. A count of the different symbols in the message can be used
# to identify the language used, and sometimes some of the letters. In English, the
# most common letter is "e", and so the symbol representing "e" should appear most
# in the encrypted text.
# Write a program that processes a string representing a message and reports the six
# most common letters, along with the number of times they appear. Case should
# not matter, so "E" and "e" are considered the same.
# Hint: There are many ways to do this. It is obviously a dictionary, but we will want
# zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
# best to ignore that initially, and then check the usual resources for the runes




# Function to get input message from the user
def inps():
    message = input("Enter your message:")
    return message

# Function to count occurrences of each alphabet character in the message
def count(message):
    letter_count = {}
    for charct in message:
        if charct.isalpha():  # Check if the value is an alphabet character
            char_lower = charct.lower()  # Convert to lowercase for uniformity
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1
    return letter_count

# Function to sort the letters by count in descending order
def main(message):
    """
    Sorts the letters in the given message by their frequency.

    Args:
    - message (str): The input message containing characters to be counted.

    Returns:
    - list: A list of tuples containing the sorted letters and their counts in descending order.

    This function counts the occurrences of each letter in the given message, 
    sorts them by their frequency in descending order, and returns the sorted list.
    """
    letter_count = count(message)
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_letters

# Function to output the six most common letters along with their counts
def outs(sorted_letters):
    print("Six most common letters and their counts:")
    for i in range(min(6, len(sorted_letters))):
        print(f"{sorted_letters[i][0]}: {sorted_letters[i][1]}")

# Get the input message
message = inps()

# Process the message and get the sorted letters by count
sorted_letters = main(message)

# Output the six most common letters along with their counts
outs(sorted_letters)




            
     