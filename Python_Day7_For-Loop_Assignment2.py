#Python program to check if a given number is an Armstrong number.

# Take input from the user
num = int(input("Enter a number: "))

# Convert the number to a string to easily iterate over digits
num_str = str(num)

# Find the number of digits
num_digits = len(num_str)

# Initialize a variable to store the sum of the powers of the digits
sum_of_powers = 0

# Calculate the sum of each digit raised to the power of the number of digits
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

# Check if the sum of the powers equals the original number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#Output
'''
Enter a number: 153
153 is an Armstrong number.
'''
