# Python - else in Loop:

# ELSE BLOCK CAN BE USED WITH BOTH FOR AND WHILE LOOP

# else clause is used along with the if statement.
# Python allows the else keyword to be used with the for and while loops too. 
# The else block appears after the body of the loop. 
# The statements in the else block will be executed after all iterations are completed. 
# The program exits the loop only after the else block is executed.

# Syntax:
# for counter in sequence:
#     Statements inside for loop block
# else:
#     Statements inside else block

# if control is not able to go in for loop, then else statement is executed

for i in range(5):
    print(i)
else:
    print("sorry no i")

for i in []:                            #in this case, interprator cant go in for loop as the list is empty, so statement in else block will be executed
    print(i)
else:
    print("sorry no i")                 #output = sorry no i

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")


# ELSE STATEMENT WILL ONLY BE EXECUTED IF LOOP IS COMPLETED, NOT IF THE LOOP IS 'BROKEN
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("sorry no i")                #here, else statement, will not be executed, because loop was 'broken'


# IN SHORT, IF LOOP IS SUCCESSFULLY COMPLETED, TILL THE LAST ITERATION THEN ONLY ELSE STATEMENT WILL BE EXECUTED


# ELSE LOOP WITH WHILE LOOP:
i = 0
while i < 7:
    print(i)
    i += 1
else:
    print("sorry no i")                #here, loop has successfully completed all iterations, so else block WILL be executed

i = 0
while i < 7:
    print(i)
    i += 1
    if i == 4:
        break
else:
    print("sorry no i")                ##here, loop has successfully completed all iterations, so else block WILL NOT be executed











