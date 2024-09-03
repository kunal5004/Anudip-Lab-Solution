#Write a Python program to remove duplicate characters of a given string.

def remove_duplicate_words(input_string):
    seen_words = set()  # Track words we've already seen
    result = []         # List to hold unique words

    # Split the input string into words
    for word in input_string.split(' '):
        # Add the word to result if it's not already seen
        if word not in seen_words:
            seen_words.add(word)
            result.append(word)
    
    # Join unique words with a space to form the final string
    return ' '.join(result)

# Input string
input_string = "String and String Function"

# Call the function and get the result
result = remove_duplicate_words(input_string)

# Print the original and the modified string
print(f"Original String: {input_string}")
print(f"String Without duplicates: {result}")

#Output
'''
Original String: String and String Function
String Without duplicates: String and Function
'''
