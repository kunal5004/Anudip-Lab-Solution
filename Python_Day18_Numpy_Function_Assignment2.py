#Suppose you have two sets of employee data—one containing information about full-time employees and another containing information about part-time employees.
#You want to combine this data to create a comprehensive employee dataset for HR analysis.

#Import Numpy Libraby
import numpy as np
#Full_time employee data
full_time_employees = np.array([

 [101, 'John Doe', 'Full-Time', 55000],

 [102, 'Jane Smith', 'Full-Time', 60000], 

[103, 'Mike Johnson', 'Full-Time', 52000] 

])
#part_time employee data
part_time_employees = np.array([

[201, 'Alice Brown', 'Part-Time', 25000], 

[202, 'Bob Wilson', 'Part-Time', 28000],

 [203, 'Emily Davis', 'Part-Time', 22000]

 ])
#Use concatenate Function to Combine both arrays
Combine=np.concatenate((full_time_employees,part_time_employees))
#Display the Result Array
print("Comprehensive Employee Dataset:")
print(Combine)

#Output
'''
Comprehensive Employee Dataset:
[['101' 'John Doe' 'Full-Time' '55000']
 ['102' 'Jane Smith' 'Full-Time' '60000']
 ['103' 'Mike Johnson' 'Full-Time' '52000']
 ['201' 'Alice Brown' 'Part-Time' '25000']
 ['202' 'Bob Wilson' 'Part-Time' '28000']
 ['203' 'Emily Davis' 'Part-Time' '22000']]
'''
