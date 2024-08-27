#Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

#take user input
User_input = input("Enter a number: ")

# Convert the user input (which is a string) to an integer
Number = int(User_input)

# Check if the number is divisible by 2 with no remainder
if Number % 2 == 0:
    # If the remainder is 0, the number is even
    print(f"{Number} is even")
else:
    # If the remainder is not 0, the number is odd
    print(f"{Number} is odd")

#output
#Enter a number: 7
#7 is odd
#Enter a number: 8
#8 is even
