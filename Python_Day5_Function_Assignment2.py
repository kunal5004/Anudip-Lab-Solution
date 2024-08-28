#Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number

# Define a function named Square_function that takes one parameter, x.
def Square_function(x):
# Calculate x raised to the power of 2 (x^2) and store the result in 'result'.
    result=(x**2)
# Return the value of 'result' to the caller of the function.    
    return result
# Call the Square_function with argument 5, and store the returned result in 'sqr'.
sqr=Square_function(5)
# Print the result using a formatted string to display the square result.
print(f"square of 5 is: {sqr}")

#output
#square of 5 is: 25
