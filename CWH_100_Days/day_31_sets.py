# Python Sets:
# Sets are UNORDERD collection of data items. 
# They store multiple items in a single variable. 
# Set items are separated by commas and enclosed within curly brackets {}. 
# Sets are UNCHANGABLE, meaning you cannot change items of the set once created.
# Sets do not contain duplicate items. MEANING, IN SET OF NAMES, IF 20 STUDENTS'S NAME IS 'RAJ', THEN 'RAJ' WILL NOT BE REPEATED 20 TIMES, IT'LL SHOW ONLY ONE TIME

info = {"Carla", 19, False, 5.9, 19}
print(info)                                                  #{False, 19, 5.9, 'Carla'},   (this is just a random order, output can also be change)
# HERE WE SEE THAT THE ITEMS OF SET OCCUR IN RANDOM ORDER AND HENCE CANNOT BE ACCESSED BY USING INDEX NUMBERS. Also sets do not allow duplicate values.


s = {2, 4, 2, 6}                                             #here, 2 is repeated twice, but in output it will be shown only once
print(s)                                                     #{2, 4, 6}                    (it is not necessary that order is always 2,4,6 may also change in output)



# Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set
shubham = {}
print(type(shubham))                                         #<class 'dict'>
# syntax of both dict and set are same,so it gives dict, for making empty set we sould do set()
shubham = set()
print(type(shubham))                                         #<class 'set'>


# Accessing set items:
# Using a For loop:
# we can access items of set using a for loop.

info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
# output:
# False
# Carla
# 19
# 5.9





































