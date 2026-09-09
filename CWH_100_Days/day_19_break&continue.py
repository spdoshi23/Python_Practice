# break statement 
# The break statement enables a program to skip over a part of the code. 
# A break statement terminates the very loop it lies within.

# example
for i in range(12):
    print("5 X", i+1, "=", 5*(i+1))
    if(i==9):
        break             # terminates the loop when i equals 10.does not print after i=10
print("loop ko chod kar nikal gaya")          

for k in range(1, 101, 1):
    print(k, end = " ")
    if(k==50):
        break
    else:           #else statement is optional. It will execute if the loop is not terminated by the break statement.
        print("mississippi")          #mississippi will be printed if break statement is not executed till that iteration.
# BREAK == EXIT THE LOOP
# CONTINUE == SKIP THE CURRENT ITERATION AND MOVE TO NEXT ITERATION

#  CONTINUE STATEMENT
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

# eg
for i in range(12):
    if(i==10):
        print("current iteration ko skip kar do")          #it'll be executed bcz it is above continue statement
        continue   
    print(i)                #this means, it will print("___") at when i=10 and then continue regularly


for i in [2, 3, 4, 6, 8, 0]:
    if i%2!=0:
        continue
    print(i)












