#Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

#Import the NumPy library
import numpy as np
#Create an array of 10 zeros in 2,5 shape.
zero=np.zeros((2,5))
#Create an array of 10 ones in 2,5 shape.
ones=np.ones((2,5))
#Create an array of 10 fives in 2,5 shape.
five=np.full((2,5),5)

#Display the array
print(zero)
print(ones)
print(five)

#Output
'''
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
[[5 5 5 5 5]
 [5 5 5 5 5]]

'''


