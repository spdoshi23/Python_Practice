# COMMENTS
# shortcut : ctrl+/
# or anything written after '#' is a commenrt
# another shortcut : anything written in triple single/dpuble quoted commas (''' or  """) is a multiline string
# eg:
print("this is print statement")   #this is a single line comment
'''
this is a multiline string. 
here we can write any number of lines in triple single inverted commas, and they will be considered as comments.
'''


# ESCAPE SEQUENCE CHARACTERS
# To insert characters that cannot be directly used in a string, we use an escape sequence character.
# like we cannot directly use dpuble inverted commas in a string inside a string thaat is sorrounded by double quotes itself
# AN ESCAPE SEQUENCE IS A BACKSLASH (\) FOLLOWED BY CHARACTER WE WANT TO INSERT
# eg:
# print("This doesnt "execute")   here we want to write "execute" but we cant directly use "". so we use \"
print("This will \"execute\"")  #output---this will "execute"
# simaliarly we can also use \' to insert single quotes in string sorrounded by single quotes

# \n---- used to break line
# eg:
print("i am a good boy\nshe is a good girl")

# PRINT
# by putting comma after "" we can add spaces, eg:
print("hi", 6, 7)

# SEPERATOR
# sep=seperator
# like it seperates hi 6 and 7 with a sign we want
# default seperator is space, eg:
print("hi", 6, 7, sep="~")   #output==hi~6~7

# END   (will learn in detail later)
# to spacify what to print at end
# eg:

print("hi", 6, 7, sep="~", end="123")    #output==hi~6~7123

# DEFAULT END IS NEW LINE
print("hi", 6, 7, sep="~", end="123")
print("shubham")    #output====hi~6~7123hi~6~7123shubham   have to mention \n to print shubham below
