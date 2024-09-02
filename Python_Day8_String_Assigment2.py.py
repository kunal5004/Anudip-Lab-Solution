# Write a Python program to remove a newline in Python, String = "\nBest \nDeeptech \nPython \nTraining\n" 

string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters
result = string.replace('\n', ' ')#Replaces each newline character \n with a space.

# Print the result
print(result.strip()) #'string' Removes any leading or trailing spaces that may result from the replacement.

#output
#Best  Deeptech  Python  Training
