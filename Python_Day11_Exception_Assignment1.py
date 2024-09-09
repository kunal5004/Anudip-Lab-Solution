# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    # Input two numbers from the user and convert them to floats
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    # Try to perform division and store the result
    result = numerator / denominator
    
    # Print the result of the division
    print(f"The result is: {result}")

# Handle the case where the denominator is zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#Output
'''
Enter the numerator: 5
Enter the denominator: 0
Error: Division by zero is not allowed.
'''
