#Python program to check if the given string is a palindrome.

# Function to check if a string is a palindrome
def is_palindrome():
# Take input from the user
    string = input("Enter a word: ").lower()
    
# Check each character from start and end
    for i in range(len(string)):
        if string[i] != string[-(i + 1)]:
            return False
    return True

# Test the function
if is_palindrome():
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")

#Output
'''    
Enter a word: racecar
This word is a palindrome.

Enter a string: stress
This word is not a palindrome.
'''
