# Write a Python program to count the occurrences of each word in a given sentence
#sentence = "To change the overall look of your document. To change the look available in the gallery"

# Convert sentence to lowercase and remove punctuation
sentence = sentence.lower().replace('.', '').replace(',', '')

# Split the sentence into words
words = sentence.split()

# Initialize a dictionary to store word counts
word_count = {}

# Count occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the results
for word, count in word_count.items():
    print(f'{word}: {count}')

#Output
'''
to: 2
change: 2
the: 3
overall: 1
look: 2
of: 1
your: 1
document: 1
available: 1
in: 1
gallery: 1
'''
