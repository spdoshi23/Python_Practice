# break statement
# The break statement enables a program to skip over a part of the code. 
# A break statement terminates the very loop it lies within.

# example
for i in range(12):
    print("5 X", i+1, "=", 5*(i+1))
    if(i==10):
        break             # terminates the loop when i equals 10.does not print after i=10
print("loop ko chod kar nikal gaya")          

for k in range(1, 101, 1):
    print(k, end = " ")
    if(k==50):
        break
    else:           #else statement is optional. It will execute if the loop is not terminated by the break statement.
        print("mississippi")
# BREAK == EXIT THE LOOP
# CONTINUE == SKIP THE CURRENT ITERATION AND MOVE TO NEXT ITERATION



