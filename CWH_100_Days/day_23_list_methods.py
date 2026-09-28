# sort()
# This method sorts the list in ascending order. The original list is updated
#  list arranges numbers in ascending order and strings in alphabetical order

# Example 1:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)                                            # ['blue', 'green', 'indigo', 'voilet']\

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)                                               # [1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]

# TO PRINT LIST IN DESCENDING ORDER:
# We must give reverse=True as a parameter in the sort method.

colors = ["voilet", "indigo", "blue", "green"]           #it will print in anti-alphabetical order
colors.sort(reverse=True)
print(colors)                                            #['voilet', 'indigo', 'green', 'blue']

num = [4,2,5,3,6,1,2,1,2,8,9,7]                          #print numbers in descending order
num.sort(reverse=True)
print(num)                                               #[9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]

# The reverse parameter is set to False by default.

# Note: Do not mistake the reverse parameter with the reverse method.
# reverse parameter - arranges in descending order 
# reverse method - entirely reverses the list, whatever the order is

# reverse()
# This method reverses the order of the list.

colors = ["voilet", "indigo", "blue", "green"]          #will reverse the entire list
colors.reverse()
print(colors)                                           #['green', 'blue', 'indigo', 'voilet']

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)                                              #[7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]

# index()
# This method returns the index of the first occurrence of the list item.
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))                            #1

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))                                     #3

# count()
# Returns the count of the number of items with the given value
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))                            #2

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]                      
print(num.count(2))                                     #3

# copy()
# Returns copy of the list. 
# This can be done to perform operations on the list without modifying the original list.
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)                                           #['voilet', 'green', 'indigo', 'blue']
print(newlist)                                          #['voilet', 'green', 'indigo', 'blue']
# now we can use append or other functions to make changes in 'newlist', without having to change the original 'colors' list.

# insert():          [IMP]
# This method inserts an item at the given index. 
# User has to specify index and the item to be inserted within the insert() method.
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1, it means that 'green'(the new element) will be inserted in such a way that it gets index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)                                           #['voilet', 'green', 'indigo', 'blue']

# extend():
# This method ADDS ENTIRE LIST OR ANY OTHER COLLECTION DATATYPE(set, tuple, dictionary) (set, tuple, dictionary) to the existing list.
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)                                           #['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

# append():
# This method appends(adds) items to the end of the existing list.
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)                                           #['voilet', 'indigo', 'blue', 'green']

# NOW IF WE WANT TO ADD A LIST TO ANOTHER LIST WITHOUT CHANGING THE ORIGINAL LIST THEN WE SHOULD USE LIST CONCATENATION, IF WE USE extend() THEN ORIGINAL LIST GETS MODIFIED

# Concatenating two lists:
# You can simply concatenate two lists to join two lists.
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)                                 #['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']












