#variables are like containers. variables are stored in memory/RAM.
# Creating a variable is like creating a placeholder in memory and assigning it some value
#example (a, c, d, b/e all 4 are diff types of variables)
a = 1
b = True
c = "Harry"
d = None
e = False
print(a)   #so basically, a = 1 was stored in ram and it was printed
print(b)   #we saved b = true in ram so when print(b) was commanded it printed 'true' as output.
    # for eg, b = true is stored in ram. and its address is given to 'b'
#WHEN YOU WANT TO PRINT VARIABLES, DONT PUT INVERTED COMMAS.
print(a+b) # here, output=2, bcz true is boolean for '1' and false is '0'.
print(a+e) #output will be 1

#a is integer. b/e are booleans. c is string. d is none types of variables.


# DATA TYPES
# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function:

f = 1   #int
print(type(a))
g = "1"  #str
print(type(g))
print(type(c))  #str

#to write complex no.   complex(8,4) = 8+4i
print(complex(8,4))

# built in data types
# 1== int (num, int, decimal, complex)
# 2== str (text) (in double quotes)
# 3== bool (t/f)

# 4==sequence data (list, tuple) (will study in later lec)
#list- mutable, tuple- immutable

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)    #[8, 2.3, [-4, 5], ['apple', 'banana']]

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)   #(('parrot', 'sparrow'), ('Lion', 'Tiger'))

#  Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within CURLY brackets.
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)   #{'name': 'Sakshi', 'age': 20, 'canVote': True}