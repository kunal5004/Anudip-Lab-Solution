#Write a Python program to get the largest and smallest number from a list without builtin functions.

# Function to find the largest and smallest numbers in a list
def find_largest_smallest(numbers):
    # Initialize largest and smallest variables to the first element of the list
    largest = numbers[0]
    smallest = numbers[0]

    # Loop through the list to compare each number
    for num in numbers:
        # If the current number is greater than the largest, update largest
        if num > largest:
            largest = num
        # If the current number is smaller than the smallest, update smallest
        if num < smallest:
            smallest = num

    # Return the largest and smallest numbers
    return largest, smallest

# Example list of numbers
numbers = [25, 14, 67, 89, 3, 45, 9]

# Call the function and store the largest and smallest values
largest, smallest = find_largest_smallest(numbers)

# Print the largest and smallest numbers
print("The largest number is:", largest)
print("The smallest number is:", smallest)

#Output
'''
The largest number is: 89
The smallest number is: 3
'''
