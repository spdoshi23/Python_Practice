# if-else Statements

# Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False.
# If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

# Based on this, the conditional statements are further classified into following types:

# if
# if-else
# if-else-elif
# nested if-else-elif.

# An if……else statement evaluates like this:
# if the expression evaluates True:
# Execute the block of code inside if statement. After execution return to the code out of the if……else block.\

# if the expression evaluates False
# Execute the block of code inside else statement. After execution return to the code out of the if……else block.

# example:
a = int(input("Enter your age: "))
if(a>=18):
    print("You can drive")              # the space(tab bar) before the print statement is important, it indicates that this line of code is part of the if statement. AND IT IS CALLED INDENTATION.
else:
    print("You cannot drive")

# CONDITIONAL OPERATORS:
# == : equal to
# != : not equal to
# < : less than
# > : greater than
# <= : less than or equal to
# >= : greater than or equal to

b = 50
print(b>50) # output= False
print(b>=50) # output= True
print(b<50) # output= False
print(b<=50) # output= True
print(b==50) # output= True
print(b!=50) # output= False

# example:
applePrice = 210
budget = 200
if (applePrice<=budget):
    print("Alexa, add 1 kg Apples to the cart")
else:
    print("Alexa, do not add Apples to the cart.")
# output= Alexa, do not add Apples to the cart.


# ELIF STATEMENTS:
# Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.

# Working of an elif statement
# Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.
# Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# .
# .
# .
# Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.

# INSHORT ELIF STATEMENTS ARE USED WHEN WE HAVE TO CHECK MULTIPLE CONDITIONS. WE CAN USE N NUMBER OF ELIF STATEMENTS IN A PROGRAM.
# THE ELSE STATEMENT IS OPTIONAL, WE CAN USE IT OR NOT, IT DEPENDS ON THE PROGRAMMER.
# PYTHON WILL GO THROUGH THE IF STATEMENT, IF IT IS FALSE THEN IT WILL CHECK THE FIRST ELIF STATEMENT, IF IT IS FALSE THEN IT WILL CHECK THE SECOND ELIF STATEMENT AND SO ON. IF ALL THE IF AND ELIF STATEMENTS ARE FALSE THEN IT WILL EXECUTE THE ELSE STATEMENT.\

# example:
num = 0
if(num<0):
    print("The number is negative")
elif(num==0):
    print("The number is zero")
else:                                     #else statement is optional, we can use it or not, it depends on the programmer. IT CANNOT TAKE CONDITIONS, IT IS USED WHEN ALL THE IF AND ELIF STATEMENTS ARE FALSE.
    print("The number is positive") 

x = int(input("Enter a number: "))
if(x<0):
    print("The number is negative")
elif(x==0):
    print("The number is zero")
elif(x==777):
    print("The number is lucky")
else:
    print("The number is positive")

# NESTED IF STATEMENTS:

# We can use if, if-else, elif statements inside other if statements as well.
# basically, we can use if statements inside other if statements. This is called nested if statements.
# example:

digit = 15
if(digit<0):
    print("The number is negative")
elif(digit>0):
    if(digit<=10):
        print("the number between 1-10")
    elif(digit>10 and digit<=20):
        print("the number is between 11-20")
    else:
        print("the number is greater than 20")
else:
    print("The number is zero")




