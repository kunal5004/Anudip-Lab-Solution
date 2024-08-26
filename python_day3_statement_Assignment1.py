#Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

# Taking a number as input from the user
number = int(input("Enter a number: "))

# Checking if the number is even or odd using a ternary operator
result = "Even" if number % 2 == 0 else "Odd"

# Printing the result
print(f"The number {number} is {result}.")

#output
#Enter a number: 3
#The number 3 is Odd.
