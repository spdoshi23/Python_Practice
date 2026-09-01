k = input("Enter a string: ")

count = 0
for char in k:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        count =  count + 1
print(count)


#                            ALTERNATE WAY TO WRITE THE ABOVE CODE

k = input("Enter a string: ")
count = 0

for char in k:
    if char in "aeiouAEIOU":
        count = count + 1   

print(count)