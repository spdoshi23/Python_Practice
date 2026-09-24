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


























