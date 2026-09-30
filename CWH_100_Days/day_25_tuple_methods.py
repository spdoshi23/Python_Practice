# Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then FIRST CONVERT TUPLE TO A LIST. 
# Then perform operation on that list and convert it back to tuple.

# Example:
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)                                #('Spain', 'Italy', 'Finland', 'Germany', 'Russia')

# Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.
# However, we can directly concatenate two tuples without converting them to list.

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)                            #('Pakistan', 'Afghanistan', 'Bangladesh', 'ShriLanka', 'Vietnam', 'India', 'China')

# Tuple methods
# As tuple is immutable type of collection of elements it have limited built in methods.

# count() Method
# The count() method of Tuple returns the number of times the given element appears in the tuple.
# SYNTAX == tuple.count(element)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)          #3

# index() method
# The Index() method returns the first occurrence of the given element from the tuple.
# SYNRTAX==tuple.index(element, start, end)
# Note: This method raises a ValueError if the element is not found in the tuple.

tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple.index(3)
print('First occurrence of 3 is', res)         #3

# TO CHECK OCCURENCE IN A PERTICULAR PORTION
res = tuple.index(3, 4, 8)
print(res)

# res = tuple.index(312)                #value error

# len()
print(len(tuple))                       #9




























