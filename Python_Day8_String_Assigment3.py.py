# Write a Python program to reverse words in a string 

String = “Deeptech Python Training”
# Given string
string = "Deeptech Python Training"

# Split the string into a list of words, then reverse the list
# [::-1] reverses the list to ['Training', 'Python', 'Deeptech']
reversed_words = string.split()[::-1]

# Join the reversed list of words into a single string with spaces in between
# ' '.join(reversed_words) results in "Training Python Deeptech"
reversed_string = ' '.join(reversed_words)

# Print the result
print(reversed_string)

#Output
#Training Python Deeptech
