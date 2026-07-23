# LENGTH OF STRINGS
# We can find the length of a string using len() function.
fruit = "Mango"
mangoLen = len(fruit)
print("Mango is a", mangoLen, "letter word.")    #mango is a 5 letter word

names = "Harry,Shubham" 
print(len(names))          #output=13

# STRING AS AN ARRAY
# A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

# SLICING:
# always use sq. brackets []
# it gives (n-1) number of characters
print(fruit[0:4])          #we get 0th, 1st, 2nd and 3rd index. we dont get 4th as it only gives n-1 characters.
# output=Mang              #including 0 but not 4, till n-1
print(fruit[1:4])          #output=ang   [index 1 to 3(n-1)]
print(fruit[:4])           #output=Mang  (python interprets 0:4 by itself)

print(fruit[:])            #output=Mango  (python interprets it as :len i.e. 0:5)

# NEGATIVE SLICING
print(fruit[0:-3])         #output=Ma    (reason---it interprets it as 0:len(fruit)-3). i.e. 0:2 
print(fruit[-1:-3])        #no output    (4:2 makes no sense)
print(fruit[-3:-1])        #output=ng    (2:4)

print(fruit[3])            #output=g     (prints 3rd index)

# SLICING FROM END
print(fruit[4:])           #output=o     (prints from 4th index to end)


nm = "Harry"
print(nm[-4:-2])           #output=ar

