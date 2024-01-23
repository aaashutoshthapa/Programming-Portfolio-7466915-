# __User Management System__

This is a simple command-line user management system implemented in Python. The system allows users 
to perform various operations such as adding a new user, checking login credentials, changing passwords, 
and deleting existing users.

## __Usage__

### Requirement 
Make sure you have Python installed on your system.

### Running the Program 
On terminal 
```
python .\task3.py .\passwd.txt  
```

## Available Commands

1. adduser: Creates a new user.
2. login:   Checks for login credentials.
3. passwd:  Changes the password for an existing user.
4. deluser: Deletes an existing user.
5. help:    Displays information about available commands.
6. exit:    Exits the command center.

## Notes

This program uses a simple custom shell-like prompt for user interaction.

Make sure to follow the correct syntax and provide the required input when prompted.

## Example of code running 

the initial looks as below:
```
C:\Users\user\OneDrive\Desktop\assignment focp\Task3>python task3.py passwd.txt
\python@python-user:~$
```

### 1. Looking at Commands Which are Avaliable
```
\python@python-user:~$  help

' adduser ' - Creates a new user
' login ' - Check for login
' passwd ' - Change Password
' deluser ' - Deletes existing user
' exit ' - exits the command center
```

### 2. Adding New user
```
\python@python-user:~$  adduser
Enter your credentials below:

>>>Enter your full name: Ada B Lovelace
>>>Enter your user name:ada
>>>Enter a password:

User created!
User ada added successfully.
```
Password is hidden which can only be seen on the txt file

### 3. loging in 
```
\python@python-user:~$  login

>>>Enter your username: ada
>>>Enter ypur password:
Login Successful! Welcome back ada
```
### 4. Other Can't Enter
```
\python@python-user:~$  login

>>>Enter your username: ada
>>>Enter ypur password:

 User not found or wrong password!!
Please check your credentials and try again!!
```



