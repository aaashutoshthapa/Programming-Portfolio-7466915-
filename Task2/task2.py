import sys

def print_header():
    print()
    print("Log File Analysis")
    print("="*20)
    print()

def read_time_data(filename):
    """
    Parameters:
    - filename (str): The name of the log file to read.

    Returns:
    - list: A list of lists containing time data from the log file. Each inner list represents a row,
    with individual elements separated by commas.
    """
    time_data = []  # Initialize an empty list to store time data
    with open(filename, "r") as file:  # Open the specified file in read mode
        for line in file:  
            lines = line.split(",")  # Split each line into a list using comma as the delimiter
            time_data.append(lines)  # Append the resulting list to the time_data list
        time_data.pop(-1)  # Remove the last element from time_data (assuming it's an empty line or unnecessary data)
    return time_data  # Return the list containing time data


def extract_entry_exit_times(time_data):
    """
    Extracts entry and exit times from a list of time data.

    Parameters:
    - time_data (list): A list containing time data for each entry, where each entry is a list.
      Each sublist is expected to have at least three elements.
    
    Returns:
    - entry_time (list): A list containing integer values representing entry times extracted from time_data.
    - exit_time (list): A list containing integer values representing exit times extracted from time_data.
    """
    # Initialize lists to store entry and exit times
    entry_time = []
    exit_time = []
    
    for i in time_data:  # Iterate through each entry in the time_data list
        entry_time.append(int(i[1]))  # Extract and convert the second element (entry time) to an integer
        exit_time.append(int(i[2]))   # Extract and convert the third element (exit time) to an integer 
    return entry_time, exit_time  #  Return the list containing entry_time and exit_time



def extract_cat_owner(filename):
    """
    Extracts cat owners from a log file.

    Parameters:
    - filename (str): The name of the log file containing cat data. The file is expected to have
      lines with comma-separated values, where each line represents an entry with at least two
      elements.

    Returns:
    - cat_owner (list): A list containing strings representing cat owners extracted from the log file.
    """
    cat_owner = []
    with open(filename, "r") as file:
        cat_data = [line.split(",") for line in file]
        cat_data.pop(-1)
        cat_owner = [entry[0] for entry in cat_data]
    return cat_owner


def count_ours_theirs(entry_exit_times, cat_owner):
    """
    Counts the number of occurrences for 'OURS' and 'THEIRS' cat owners based on entry and exit times.

    Parameters:
    - entry_exit_times (list): A list containing time differences for each entry.
    - cat_owner (list): A list containing strings representing cat owners for each entry. 
      Each entry corresponds to a cat owner, and the order should match the entry_exit_times.

    Returns:
    - ours (int): The count of occurrences where the cat owner is 'OURS'.
    - theirs (int): The count of occurrences where the cat owner is 'THEIRS'.

    """
    # Initializing counters for "OURS" and "THEIRS" categories
    ours = 0
    theirs = 0
    
    for i, time_difference in enumerate(entry_exit_times):  # Iterating through entry_exit_times and corresponding cat_owners
        # Checking the cat owner category
        if cat_owner[i] == "THEIRS":  
            theirs += 1
        elif cat_owner[i] == "OURS":
            ours += 1       
    return ours, theirs  # Returning the counts of "OURS" and "THEIRS" categories


def calculate_time_stayed(entry_exit_times, cat_owner):
    """
    Calculates the total time stayed by 'OURS' cat owners based on entry and exit times.

    Parameters:
    - entry_exit_times (list): A list containing time differences for each entry.
    - cat_owner (list): A list containing strings representing cat owners for each entry. 
      Each entry corresponds to a cat owner, and the order should match the entry_exit_times.

    Returns:
    - time_stayed (int): The total time stayed by 'OURS' cat owners.
    """
    time_stayed = 0  # Initializing a variable to track the total time stayed for "OURS" category
    
    for i in range(len(entry_exit_times)):  # Iterating through entry_exit_times and corresponding cat_owners
        if cat_owner[i] == "OURS":   # Accumulating time stayed if the cat owner category is "OURS"
            time_stayed += entry_exit_times[i]
    return time_stayed  # Returning the total time stayed for "OURS" category


def calculate_average_time(entry_exit_times, cat_owner):
    """
    Calculates the average time stayed by 'OURS' cat owners based on entry and exit times.

    Parameters:
    - entry_exit_times (list): A list containing time differences for each entry.
    - cat_owner (list): A list containing strings representing cat owners for each entry. 
      Each entry corresponds to a cat owner, and the order should match the entry_exit_times.

    Returns:
    - average (int): The average time stayed by 'OURS' cat owners. If there are no 'OURS' entries, 
      the function returns 0.
    """
    # Initializing variables to track the total sum and entry count for "OURS" category
    total_sum = 0
    total_entry = 0
    
    # Iterating through entry_exit_times and corresponding cat_owners
    for i, time_difference in enumerate(entry_exit_times):
        if cat_owner[i] == "OURS":  # Accumulating time difference and counting entries if the cat owner category is "OURS"
            total_sum += time_difference
            total_entry += 1

    average = total_sum // total_entry if total_entry != 0 else 0  # Calculating the average time stayed for "OURS" category, handling division by zero
    return average  # Returning the calculated average


def main():
    """
    Main function for analyzing cat visit data.

    This function orchestrates the analysis of cat visit data from a specified log file.
    It extracts relevant information, such as entry and exit times, cat owners, and calculates
    various statistics including the number of visits, total time in the house, average visit duration,
    and the longest and shortest visits.

    The log file should be formatted with each line representing a cat visit entry, with at least
    three elements: cat owner, entry time, and exit time.

    Command Line Arguments:
    - sys.argv[1] (str): The filename of the log file containing cat visit data.

    Output:
    The function prints the following statistics to the console:
    - Number of visits by 'OURS' cats.
    - Number of visits by 'THEIRS' cats.
    - Total time spent in the house in hours and minutes.
    - Average visit duration in minutes.
    - Longest visit duration in minutes.
    - Shortest visit duration in minutes.
    """
    print_header()  # Print header information

    filename = sys.argv[1]  # Get the filename from the command-line argument
    
    # Read and process time data
    time_data = read_time_data(filename)
    entry_time, exit_time = extract_entry_exit_times(time_data)
    cat_owner = extract_cat_owner(filename)
    
    # Calculate time differences
    time_difference = [exit_time[i] - entry_time[i] for i in range(len(entry_time))]

    # Count "OURS" and "THEIRS" occurrences
    ours, theirs = count_ours_theirs(time_difference, cat_owner)
    time_stayed = calculate_time_stayed(time_difference, cat_owner)

    # Calculate total time stayed and convert it to hours and minutes
    hours = time_stayed // 60
    minutes = time_stayed % 60

    # Create a modified time_difference list for "OURS" entries
    ours_time_difference = time_difference[:]
    for i, j in enumerate(time_difference):
        if cat_owner[i] == "THEIRS":
            ours_time_difference[i] = 1441

    # Find the longest and shortest visit times
    longest_time = max(time_difference)
    shortest_time = min(ours_time_difference)

    # Calculate the average visit time
    average = calculate_average_time(time_difference, cat_owner)

    # Print the summary statistics
    print(f"Cat visits: {ours}")
    print(f"Other Cats: {theirs}")
    print(f"Total Time in House: {hours} hours {minutes} minutes\n")
    print(f"Average visit: {average} minutes")
    print(f"longest visit: {longest_time} minutes")
    print(f"Shortest visit: {shortest_time} minutes")

if __name__ == "__main__":
    main()
