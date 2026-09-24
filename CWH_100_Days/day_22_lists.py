# Python Lists

# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.
# LISTS CAN BE CHANGED, TUPELS CAN'T BE CHANGED

marks = [1, 2, 3] 
print(type(marks))                    #<class 'list'>
print(marks[0]) #(0th index)          #1
print(marks[1])                       #2
print(marks[2])                       #3


lst1 = [1,2,2,3,5,4,6]                        #[1, 2, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]               #['Red', 'Green', 'Blue']
print(lst1)
print(lst2)

details = ["Abhijit", 18, "FYBScIT", 9.8]
print(details)                                #['Abhijeet', 18, 'FYBScIT', 9.8]
# a single list can contain items of different data types.


# List Index
# each item/element in a list has its own unique index.
#  This index can be used to access any particular item from the list. 
# The first item has index [0], second item has index [1], third item has index [2] and so on

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]


# Accessing list items :
# We can access list items by using its index with the square bracket syntax [].
#  For example colors[0] will give "Red", colors[1] will give "Green" and so on...

# Positive Indexing:
# As we have seen that list items have index, as such we can access items using these indexes.

# Example:
print(colors[2])             #Blue
print(colors[3])             #Yellow
print(colors[0])             #Red

# Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, BUT FROM THE END OF THE LSIT
# THE LAST ITEM HAS INDEX AS [-1],
# SECOND LAST ITEM HAS INDEX AS [-2],
# SIMILIARLY THIRD LAST AS [-3], AND SO ON

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
#          [0]      [1]     [2]      [3]      [4]

# EASY METHOD:
print(colors[-2])                        #negative, -2
print(colors[len(colors)-2])             #positive, 5-2 = 3

print(colors[-1])            #Green
print(colors[-3])            #Blue
print(colors[-5])            #  Red


# Check whether an item in present in the list?
# We can check if a given item is present in the list.
#  This is done using the 'in' keyword.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")               # Yellow is present

if "orange" in colors:
    print("orange is present.")
else:
    print("orange is absent.")               #orange is absent.

# SAME THING APPLIES FOR STRING AS WELL
if "bha" in "shubham":
    print("yes")
else:
    print("no")                          #yes

if "bhu" in "shubham":
    print("yes")
else:
    print("no")                         #no
    

# Range of Index:
# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range

# SYNTAX:  listName[start : end : jumpIndex]
# Note: jump Index is optional. We will see this in later examples.

print(colors[1:4:2])              # ['Green', 'Yellow']

# Example: printing elements within a particular range:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	              #using positive indexes,       ['mouse', 'pig', 'horse', 'donkey']
print(animals[-7:-2])	          #using negative indexes'       ['bat', 'mouse', 'pig', 'horse', 'donkey']
# Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.

# Note: The element of the end index provided will not be included.  it prints n-1 indicies

# Example: printing all element from a given index till the end
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes              ['pig', 'horse', 'donkey', 'goat', 'cow']
print(animals[-4:])	#using negative indexes              ['horse', 'donkey', 'goat', 'cow']
# When no end index is provided, the interpreter prints all the values till the end.

# Example: printing all elements from start to a given index
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes          ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
print(animals[:-3])	#using negative indexes          ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
# When no start index is provided, the interpreter prints all the values from start up to the end index provided.

# Example: Printing alternate values
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes           ['cat', 'bat', 'pig', 'donkey', 'cow']
print(animals[-8:-1:2])	#using negative indexes           ['dog', 'mouse', 'horse', 'goat']
# Here, we have not provided start and index, which means all the values will be considered. 
# But as we have provided a jump index of 2 only alternate values will be printed.


# List Comprehension:
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:          List = [Expression(item) for item in iterable if Condition]
#                  new_list = [WHAT_TO_PUT_IN_LIST for VARIABLE in SOMETHING] 
# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not.
lst = [i for i in range(4)]  
print(lst)                        #[0, 1, 2, 3]
 
lst = [i*i for i in range(4)]
print(lst)                        #[0, 1, 4, 9]  

lst = [i*i for i in range(10)]
print(lst)                        #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

lst = [i*i for i in range(10) if i%2==0]
print(lst)                        #[0, 4, 16, 36, 64]

# Example 1: Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)                #['Milo', 'Bruno', 'Rosa']

# Example 2: Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)                #['Sarah', 'Bruno', 'Anastasia']



















































