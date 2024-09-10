#Write a Python program to find duplicate values from a list and display those

# Function to find duplicate values in a list
def find_duplicates(numbers):
    duplicates = []  # List to store duplicate values
    seen = []        # List to track numbers already checked

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)  # Add to duplicates if already seen and not added
        else:
            seen.append(num)        # Add to seen list if first time

    return duplicates

# Example list of numbers
numbers = [10, 20, 30, 40, 20, 50, 10, 60, 40]

# Call the function to find duplicates
duplicates = find_duplicates(numbers)

# Print the duplicate values
print("Duplicate values:", duplicates)

#output
#Duplicate values: [20, 10, 40]
