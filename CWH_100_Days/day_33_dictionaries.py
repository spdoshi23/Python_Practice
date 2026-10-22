# Python Dictionaries:
# Dictionaries are ordered collection of data items. 
# They store multiple items in a single variable. 
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# dict = {key : value}

dic = {
    "Shubham": "Human being", 
    "Spoon": "Object"
}
print(dic["Shubham"])                                           #Human being
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)                                                     #{'name': 'Karan', 'age': 19, 'eligible': True}


# Accessing Dictionary items:

# I. Accessing single values:
# Values in a dictionary can be accessed using keys. 
# We can access dictionary values by mentioning keys either in square brackets or by using get method.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])                                             #Karan
print(info.get('eligible'))                                     #True
# if we want to throw an error for nor-existing key in dictionary, then use [] method, if we dont want error to occur then use .get() method{.get() method gives'none' for non existing key}

# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())                                            #dict_values(['Karan', 19, True])

# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())                                               #dict_keys(['name', 'age', 'eligible'])

# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())                                              #dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])




















































