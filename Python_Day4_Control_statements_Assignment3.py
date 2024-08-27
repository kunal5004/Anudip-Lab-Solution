#Write a Python program that determines if a given year is a leap year or not.
# user input to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # If the year is divisible by 4 and not divisible by 100,
    # or if it is divisible by 400, it is a leap year
    print(f"{year} is a leap year.")
else:
    # If the conditions are not met, it is not a leap year
    print(f"{year} is not a leap year.")

#output
#Enter a year: 2002
#2002 is not a leap year.
#Enter a year: 2020
#2020 is a leap year.
