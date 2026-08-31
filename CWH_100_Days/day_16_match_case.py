# MATCH CASE STATEMENT:
# To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python
# 
# A match statement will compare a given variable’s value to different shapes, also referred to as the pattern.
#  The main idea is to keep on comparing the variable with all the present patterns until it fits into one.
# The match case consists of three main entities :

#1. The match keyword
#2. One or more case clauses
#3. Expression for each case
# The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

x = 4
match x:
    #if x is 0
    case 0:
        print("x is zero")
    case 4:
        print("x is four")


x = int(input("Enter a number: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _:
        print(x)             # if x is not 0 or then it'll print x itself. as _ is considered as a default case in match case statement. It is similar to else statement in if-else statement.

#  in python, whichever case matches first, the corresponding block of code will be executed.
#  If none of the cases match, the default case (case _) will be executed.
# and once if any case matches, the control will exit the match statement and will not check for any other cases below it.

x = int(input("Enter a number: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if x!=90:
        print(x, "is not 90")  # if x is not 0 or 4 and also not equal to 90, then it'll print x itself. as _ is considered as a default case in match case statement. It is similar to else statement in if-else statement.
    case _ if x!=80:
        print(x, "is not 80")  # if x is not 0 or 4 and also not equal to 80, then it'll print x itself. as _ is considered as a default case in match case statement. It is similar to else statement in if-else statement.
# in above eg, if x = 56, then it'll print "56 is not 90" and will not check for the next case. because whichever case matches first, the corresponding block of code will be executed and once if any case matches, the control will exit the match statement and will not check for any other cases below it.
# if x = 90 then only it'll check the second condition of default case (_)>


# IF YOU ARE MATCHING A NUMBER, YOU DON'T NEED TO SORROUND IT WITH "" WHILE WRITING CASE STATEMENT. 
# BUT WHILE MATCHING STRINGS YOU HAVE TO SORROUND THEM WITH "" WHILE WRITING CASE STATEMENT.  (refer day_16_calc.py to understand)



