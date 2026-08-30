import time
#  strftime() is a function in the time module that formats a time object into a string representation based on a specified format.
#  It allows you to customize how the date and time are displayed.
# INSHORT STRFTIME() IS A FUNCTION WHICH GIVES US THE CURRENT TIME AND DATE IN A SPECIFIC FORMAT.
current_time = time.strftime('%H:%M:%S')  # %H: Hour (00-23), %M: Minute (00-59), %S: Second (00-59)
print("Current time is", current_time)
current_hour = int(time.strftime('%H'))
print("Current hour is", current_hour)
current_minute = time.strftime('%M')
print("Current minute is", current_minute)
current_second = time.strftime('%S')
print("Current second is", current_second)

if 4<current_hour<10:
    print("Good Morning")
elif 10<=current_hour<16:
    print("Good Afternoon")
elif 16<=current_hour<20:
    print("Good Evening")
else:
    print("Good Night")

# WE HAD TO USE int() FUNCTION TO CONVERT THE STRING VALUE OF HOUR INTO INTEGER BECAUSE WE CANNOT USE CONDITIONAL OPERATORS ON STRING VALUES. SO WE CONVERTED THE STRING VALUE OF HOUR INTO INTEGER VALUE USING int() FUNCTION.
# THIS WAS THE CATCH OF THIS PROGRAM. IF WE DIDN'T CONVERT THE STRING VALUE OF HOUR INTO INTEGER VALUE THEN THE PROGRAM WOULD HAVE THROWN AN ERROR.

# to learn time module in python:
# https://docs.python.org/3/library/time.html#time.strftime






