#Write a Python program to Get Only unique items from two sets. 

#Input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#Get the unique items using union
unique_items = set1 | set2

#Output the unique items
print(unique_items)

#Output
#{70, 40, 10, 50, 20, 60, 30}
