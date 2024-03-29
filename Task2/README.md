# __Log File Analysis__

## __Overview__
This Python script analyzes cat visit data from a specified log file. The log file should be formatted with each 
line representing a cat visit entry, including at least three elements: cat owner, entry time, and exit time. 
The script extracts relevant information, such as entry and exit times, cat owners, and calculates various statistics, 
including the number of visits, total time in the house, average visit duration, and the longest and shortest visits.

## __Usage__
To use the script, run it from the command line with the log file as a command-line argument. For example:
```
python .\task2.py .\shelter_2023-08-25.log
```

## __Command Line Arguments__
sys.argv[1] (str): The filename of the log file containing cat visit data.

## __Output__
The script prints the following statistics to the console:

Number of visits by 'OURS' cats.
Number of visits by 'THEIRS' cats.
Total time spent in the house in hours and minutes.
Average visit duration in minutes.
Longest visit duration in minutes.
Shortest visit duration in minutes.

### 1. Handelling of Command Line Argument
#### Missing command line argument
```
PS C:\Users\user\OneDrive\Desktop\assignment focp\Task2> python .\task2.py

Log File Analysis
====================

Error: Missing filename argument. Please provide the filename of the log file.
```

#### Wrong File Name 
```
PS C:\Users\user\OneDrive\Desktop\assignment focp\Task2> python .\task2.py file_that_does_not_exist.log

Log File Analysis
====================

Error: File 'file_that_does_not_exist.log' not found. Please provide a valid log file.
```
### 2. Output of shelter_2023-08-25
```
PS C:\Users\user\OneDrive\Desktop\assignment focp\Task2> python .\task2.py .\shelter_2023-08-25.log

Log File Analysis
====================

Cat visits: 12
Other Cats: 58
Total Time in House: 4 hours 5 minutes

Average visit: 20 minutes
longest visit: 45 minutes
Shortest visit: 5 minutes
```

### 3. Output of shelter_2023-08-26
```
PS C:\Users\user\OneDrive\Desktop\assignment focp\Task2> python .\task2.py .\shelter_2023-08-26.log

Log File Analysis
====================

Cat visits: 11
Other Cats: 45
Total Time in House: 5 hours 0 minutes

Average visit: 27 minutes
longest visit: 45 minutes
Shortest visit: 10 minutes
```

### 4. Output of shelter_2023-08-27
```
PS C:\Users\user\OneDrive\Desktop\assignment focp\Task2> python .\task2.py .\shelter_2023-08-27.log

Log File Analysis
====================

Cat visits: 13
Other Cats: 53
Total Time in House: 5 hours 50 minutes

Average visit: 26 minutes
longest visit: 50 minutes
Shortest visit: 5 minutes
```
# __SO THIS COMPLETES TASK 2 WHICH HELPS TO FIND THE OUTPUT OF CATS BASED ON VISIT__




