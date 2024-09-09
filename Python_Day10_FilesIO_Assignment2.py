#Write a function in Python to count and display the total number of words in a text file “ABC.txt”
def count_words_in_file():
    try:
        with open("ABC.txt", "r") as file:
            # Read the entire file content
            content = file.read()
            # Split the content into words based on whitespace
            words = content.split()
            # Count the number of words
            word_count = len(words)
            print(f"Total number of words in 'ABC.txt': {word_count}")
    except FileNotFoundError:
        print("The file ABC.txt does not exist.")

# Call the function
count_words_in_file()

#Output
#Total number of words in 'ABC.txt': 9
