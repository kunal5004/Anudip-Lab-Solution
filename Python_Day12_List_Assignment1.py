#Write a Python program to sum all the items in a list.

# Define a function that takes a list of numbers as input
def sum_of_list(numbers):
    # Use the built-in sum() function to calculate the sum of all items in the list
    return sum(numbers)

# Example list of numbers
numbers = [10, 20, 30, 40, 50]

# Call the sum_of_list function with the 'numbers' list and store the result in 'result'
result = sum_of_list(numbers)

# Print the sum of the list
print("The sum of the list is:", result)

#Output
#The sum of the list is: 150
