#Write a Python program to Return a set of elements present in Set A or B, but not both.

#Input set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_set= set1^set2
print(unique_set)

#Output
#{20, 70, 10, 60}
