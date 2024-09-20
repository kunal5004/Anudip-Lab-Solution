#Compute the standard deviation of the NumPy array
#Import the numpy library
import numpy as np
#Input the array
arr = np.array([20, 2, 7, 1, 34])
#find variance using Var function
variance=np.var(arr)
#Dislplay Orginal array & Variance
print("Array:",arr)
print(f"Variance: {variance}")
#Use std() function for standard deviation
Stdv=np.std(arr)
#Display Standard deviation
print(f"Standard deviation: {Stdv}")

#Output
'''
Array: [20  2  7  1 34]
Variance: 158.16
Standard deviation: 12.576167937809991
'''
