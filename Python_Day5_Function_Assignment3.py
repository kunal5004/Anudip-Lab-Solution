#Using max() and min() functions display the maximum and minimum of 5 random numbers.


# Import the random module to generate random numbers.
import random
# Generate a list of 5 random numbers between 1 and 100.
random_numbers = [random.randint(1, 100) for i in range(5)]
# Display the list of random numbers.
print(f"Random numbers: {random_numbers}")
# Find the maximum value among the random numbers using max().
max_value = max(random_numbers)
# Find the minimum value among the random numbers using min().
min_value = min(random_numbers)
# Display the maximum and minimum values.
print(f"Maximum of the random numbers is: {max_value}")
print(f"Minimum of the random numbers is: {min_value}")

#Output
'''
Random numbers: [76, 63, 16, 93, 3]
Maximum of the random numbers is: 93
Minimum of the random numbers is: 3
'''
