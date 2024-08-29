def is_palindrome(x):
# Convert the number to a string    
    str_num=str(x)
# Reverse the string and compare with the original string
    if str_num == str_num[::-1]:
        return True
    else:
        return False
# Input from the user
num=int(input("Enter a number: "))
# Check if the number is a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#Output
'''    
Enter a number: 15851
15851 is a palindrome.

Enter a number: 1234
1234 is not a palindrome.
'''
