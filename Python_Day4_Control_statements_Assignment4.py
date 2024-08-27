#Create a Python program that checks if a user-given number is positive, negative, or zero.
# Prompt the user to enter a number
number = float(input("Enter a number: "))

# Check if the number is positive
if number > 0:
    print(f"{number} is positive.")
# Check if the number is negative
elif number < 0:
    print(f"{number} is negative.")
# If neither condition is true, the number must be zero
else:
    print("The number is zero.")

#output
#Enter a number: 10
#10.0 is positive.
#Enter a number: -5
#-5.0 is negative.
#Enter a number: 0
#The number is zero.   
