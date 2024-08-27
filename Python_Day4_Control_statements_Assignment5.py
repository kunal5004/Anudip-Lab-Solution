#Write a Python program that determines the largest of three numbers entered by the user.
#user input to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Check which number is the largest
# If num1 is greater than or equal to both num2 and num3, it is the largest
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
# If num2 is greater than or equal to both num1 and num3, it is the largest    
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")
# If neither num1 nor num2 is the largest, the third number must be the largest
else:
    print(f"The largest number is: {num3}")

#output
#Enter the first number: 3
#Enter the second number: 8
#Enter the third number: 2
#The largest number is: 8.0    
