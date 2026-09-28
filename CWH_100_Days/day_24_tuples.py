# Python Tuples
# Tuples are ordered collection of data items. 
# They store multiple items in a single variable. 
# Tuple items are separated by commas and enclosed within round brackets (). 
# Tuples are unchangeable meaning we can not alter them after creation.

tup = (1, 5, 6)
print(type(tup))                                    #<class 'tuple'>

# Example 1:
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)                                       #(1, 2, 2, 3, 5, 4, 6)
print(tuple2)                                       #('Red', 'Green', 'Blue')

# Example 2:
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)                                      #('Abhijeet', 18, 'FYBScIT', 9.8)

# Tuple Indexes
# Each item/element in a tuple has its own unique index. 
# This index can be used to access any particular item from the tuple. 
# The first item has index [0], second item has index [1], third item has index [2] and so on.

country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]              

# Accessing tuple items:
# I. Positive Indexing:
# As we have seen that tuple items have index, as such we can access items using these indexes.

country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]     
print(country[0])                                   #Spain
print(country[1])                                   #Italy
print(country[2])                                   #India

# II. Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. 
# The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1]),  Germany
print(country[-3])                                  #India
print(country[-4])                                  #Italy

# III. Check for item:
# We can check if a given item is present in the tuple. 
# This is done using the 'in' keyword.

country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")                     #Germany is present.

country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")                      #Russia is absent.

# IV. Range of Index:
# You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.
# Syntax:
# Tuple[start : end : jumpIndex]
# jump Index is optional.

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes      ('mouse', 'pig', 'horse', 'donkey')
print(animals[-7:-2])   #using negative indexes      ('bat', 'mouse', 'pig', 'horse', 'donkey')

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes      ('pig', 'horse', 'donkey', 'goat', 'cow')
print(animals[-4:])     #using negative indexes      ('horse', 'donkey', 'goat', 'cow')

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes      ('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
print(animals[:-3])     #using negative indexes      ('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes      ('cat', 'bat', 'pig', 'donkey', 'cow')
print(animals[-8:-1:2]) #using negative indexes      ('dog', 'mouse', 'horse', 'goat')

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])                               #('dog', 'pig', 'goat')










