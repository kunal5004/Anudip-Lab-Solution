# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    # Prompt the user to input an integer
    user_input = input("Enter an integer: ")

    # Attempt to convert the input to an integer
    user_input = int(user_input)

    # If conversion is successful, print the integer
    print(f"You entered the integer: {user_input}")

# Handle the case where the input is not a valid integer
except ValueError:
    print("Error: The input is not a valid integer.")

#Output
'''
Enter an integer: 4.2
Error: The input is not a valid integer.
'''
