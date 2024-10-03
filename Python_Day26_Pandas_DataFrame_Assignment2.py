# Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. 
#Import pandas and numpy Library
import numpy as np
import pandas as pd
#Input columns and values
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

#Create DataFrame and Index
df = pd.DataFrame(exam_data, index=['Student_1 ', 'Student_2', 'Student_3', 'Student_4', 'Student_5', 
                                    'Student_6', 'Student_7', 'Student_8', 'Student_9', 'Student_10'])
#Display DataFrame
print(df)

#Output
'''
                 name  score  attempts qualify
Student_1   Anastasia   12.5         1     yes
Student_2        Dima    9.0         3      no
Student_3   Katherine   16.5         2     yes
Student_4       James    NaN         3      no
Student_5       Emily    9.0         2      no
Student_6     Michael   20.0         3     yes
Student_7     Matthew   14.5         1     yes
Student_8       Laura    NaN         1      no
Student_9       Kevin    8.0         2      no
Student_10      Jonas   19.0         1     yes

'''
