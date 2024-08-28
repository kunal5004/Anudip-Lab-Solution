#Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

#First we define fucntion and give parameters x and y.
def Div_function(x,y):
# Perform division of x by y and store the result in the variable 'result'.
    result=x/y
# Return the value of 'result' to the caller of the function.    
    return result
# Call the Div_function with arguments 10 and 5, and store the returned result in 'div'.
div=Div_function(10,5)
# Print the result using formatted string to display the division result.
print(f"The division of the two numbers is: {div}")

#output
#The division of the two numbers is: 2.0
