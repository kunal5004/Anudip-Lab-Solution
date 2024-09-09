#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
def create_and_read_file():
    # Create and write to the file
    with open("ABC.txt", "w") as file:
        file.write("Good Morning.\n")
        file.write("I am Kunal.\n")
        file.write("have a great day!.\n")
# Read and display the file content
    try:
        with open("ABC.txt", "r") as file:
            for line in file:
                print(line.strip())  # strip() removes any extra newline characters
    except FileNotFoundError:
        print("The file ABC.txt does not exist.")

# Call the function
create_and_read_file()

#Output
'''
Good Morning.
I am Kunal.
have a great day!.
'''
