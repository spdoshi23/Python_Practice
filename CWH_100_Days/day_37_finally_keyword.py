# Finally Clause
# The finally code block is also a part of exception handling. 
# When we handle exception using the try and except block, we can include a finally block at the end. 
# The finally block is ALWAYS EXECUTED, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

# Syntax:
# try:
   #statements which could generate 
   #exception
# except:
   #solution of generated exception
# finally:
    #block of code which is going to 
    #execute in any situation
    
# The finally block is executed irrespective of the outcome of try……except…..else blocks
# One of the important use cases of finally block is in a function which returns a value.

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")

# outputs:
# Enter an integer: 19                            Enter an integer: 3.142
# Integer Accepted.                               Number entered is not an integer.
# This block is always executed.                  This block is always executed.

def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except Exception as e:
        print(e)
        print("Some errror occured")
        return 0
    finally:
        print("i am always executed")            #this will be executed even if func has already returned a value
x = func1
print(x)

# finally KEYWORD IS MAINLY USED IN FUNCTIONS TO EXECUTE SOMETHING EVEN AFTER RETURNING A VALUE ALREADY




















