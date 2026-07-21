#  we can take user input directly by using input() function.
# This input function gives a return value as string/character hence we have to pass that into a variable

a = input()                   # first it will ask you to write your name in terminal.
print ("my name is", a)       # as soon as i write my name, it'll give output as: my name is shubham

#we can also add string in input function as follows:
b = input("what is your name  ")   #output: what is your name___
print("my name is", b)           #after iwrite my name, output: my name is ____

# IMPORTANT----  input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

x = input("enter first number:  ")    #let 1st no. be 5
y = input("enter second number:  ")   #let 2nd no. be 5
print(x+y)                            #even though we have added 5 with 5 it will give output as 55 and not 10. 
                                      #it happend bcz intut function returns value as string. we have to typecast it to int to get correct ans.
print(int(x)+float(y))                  #now output: 10.0

#alternate way
p = int(input("enter first number:  "))
q = float(input("enter second number:  "))
print(p+q)                                     #this keeps variable p and q as int and float in entire code.

