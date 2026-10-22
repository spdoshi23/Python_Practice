# Joining Sets:
# Sets in python more or less work in the same way as sets in mathematics.
# We can perform operations like union and intersection on the sets just like in mathematics.

s1 = {1, 2, 5, 6}
s2 = {3 ,6 ,7}
print(s1.union(s2))                                                  
s1.update(s2)
print(s1)

# I. union() and update()    AUB:   
# The union() and update() methods prints all items that are present in the two sets. 
# The union() method returns a new set whereas update() method adds item into the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)                                                       #{'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)                                                        #{'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'} 
 

# II. intersection and intersection_update()     AintersectionB:
# The intersection() and intersection_update() methods prints only items that are similar to both the sets.
# The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)                                                       #cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)                                                        #{'Tokyo', 'Madrid'}


# III. symmetric_difference and symmetric_difference_update()      AUB - AintersectionB:
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. 
# The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)                                                       #{'Seoul', 'Kabul', 'Berlin', 'Delhi'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)                                                        #{'Kabul', 'Delhi', 'Berlin', 'Seoul'}

# IV. difference() and difference_update()     A-B:
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. 
# The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)                                                       #{'Tokyo', 'Madrid', 'Berlin'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities.difference_update(cities2)                                    #{'Tokyo', 'Berlin', 'Madrid'}
print(cities)



# Set Methods:
# There are several in-built methods used for the manipulation of set.

# isdisjoint():
# The isdisjoint() method checks if items of given set are present in another set. 
# This method returns False if items are present, else it returns True.
# disjoint sets are sets which dont have any intersection in between them

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))                                     #False

cities = {"tokyo", "madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))                                     #True, bcz now they dont have anything ina common


# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. 
# It returns True if all the items are present, else it returns False.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))                                    #False
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))                                    #False
cities4 = {"Madrid","Delhi"}
print(cities.issuperset(cities4))                                    #True 


# issubset():
# The issubset() method checks if all the items of the original set are present in the particular set.
# It returns True if all the items are present, else it returns False.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))                                      #True
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Madrid"}
print(cities2.issubset(cities))                                      #False


# add()
# If you want to add a single item to the set use the add() method.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)                                                        #{'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}


# update()
# If you want to ADD MORE THAN ONE ITEM, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)                                                       #{'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}


# remove()/discard()
# We can use remove() and discard() methods to remove items form list.

# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() RAISES AN ERROR, whereas discard() DOES NOT RAISE AN ERROR.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)                                                       #{'Delhi', 'Berlin', 'Madrid'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Seoul")
# print(cities)                                                       #KeyError: 'Seoul'


# pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. 
# However, you can access the popped item if you assign the pop() method to a variable.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)                                                       #{'Madrid', 'Berlin', 'Tokyo'}
print(item)                                                         #Delhi


# del
# del is not a method, rather it is a keyword which deletes the set entirely.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)                                                       #NameError: name 'cities' is not defined

# We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

# What if we don’t want to delete the entire set, we just want to delete all items within that set?
# then we use clear method


# clear():
# This method clears all items in the set and prints an empty set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)                                                         #output = set()


# Check if item exists
# You can also check if an item exists in the set or not.

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
# Carla is present.



























