#Write a Python program to Count all letters, digits, and special symbols from the given string

# Define a function to count letters, digits, and special symbols in a string
def count_characters(input_string):
    # Initialize counters for letters (Chars), digits (Digits), and special symbols (symbols)
    Chars = 0
    Digits = 0
    symbols = 0

    # Iterate over each character in the input string
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            Chars += 1
        # Check if the character is a digit
        elif char.isdigit():
            Digits += 1
        # If the character is neither a letter nor a digit, it is considered a special symbol
        else:
            symbols += 1

    # Return the counts of letters, digits, and special symbols as a tuple
    return Chars, Digits, symbols

# Define the input string to analyze
input_string = "P@#yn26at^&i5ve"

# Call the count_characters function and unpack the result into Chars, Digits, and symbols
Chars, Digits, symbols = count_characters(input_string)

# Print the results
print(f"Chars: {Chars}")    # Output the count of letters
print(f"Digits: {Digits}")  # Output the count of digits
print(f"Symbols: {symbols}") # Output the count of special symbols

#Output
'''
Chars: 8
Digits: 3
Symbols: 4
'''
