#def function
def factorial(n):
    # Check if the input is negative
    if n<0:
        return
# Initialize the result variable to 1
    result = 1
# Use a while loop to calculate the factorial
    while n>0:
# Multiply result by the current value of n
        result *=n
# Decrease the value of n by 1
        n-=1
# Return the computed factorial
    return result
# Get user input
num=int(input("Enter a number: "))
# Calculate and print the factorial of the given number
print(f"the factorial of {num} is {factorial(num)}")

#Output
'''
Enter a number: 5
the factorial of 5 is 120
'''
