# Exception Handling:
# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. 
# Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

# Exceptions in Python:
# Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).
# When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. 
# If not handled, the program will crash.

# Python try...except:
# try….. except blocks are used in python to handle errors and exceptions. 
# The code in try block runs when there is no error. 
# If the try block catches the error, then the except block is executed.

# SYNTAX:
# try:
     #statements which could generate 
     #exception
# except:
     #Soloution of generated exception

try:
    num = int(input("Enter an integer: "))
    k = [4,6]
except ValueError:                                       #we can handle different type of errors differently BY ADDING MULTILE except BLOCKS
    print("Number entered is not an integer.")
except IndexError:
    print("index error")

# Output:
# Enter an integer: 6.022
# Number entered is not an integer.

try:
    a = input("Enter a number : ")                       #here, there is a PROBABILITY of error, bcz if uses enters something else than integer, then entire code below this live will break
    print(f"multiplication table of {a} is:")
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:                                   #used as a template to handle exception and know which type of exception
    print(e)
    print("invalid input")

# IF THERE ARE 50 LINES WRITTEN IN try BLOCK AND EXCEPTION OCCURS IN 10TH LINE THEN, THE CONTROL GOES TO THE except BLOCK AND SAVES THE ENTIRE CODE FROM BREAKING














