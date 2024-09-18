#Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

#Import numpy librabry
import numpy as np

#Input list 
list1=[1,2,3,4,5]

#Convert list to array
my_array=np.array(list1)

#Display array
print("Array: ", my_array)
#Display array first index position (0)
print("First element: ", my_array[0])
#Display array Last index position (-1)
print("Last element: ", my_array[-1])

#Multiply array by 2 and display array
Mul_array= my_array * 2
print("Array after Multiplication: ", Mul_array)

#Output
'''
Array:  [1 2 3 4 5]
First element:  1
Last element:  5
Array after Multiplication:  [ 2  4  6  8 10]
'''
