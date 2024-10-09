#.Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school.
#Also generate a horizontal bar chart based on the result and explain the conclusion.

import pandas as pd
import matplotlib.pyplot as plt

# Input data
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12], 
    'height': [173, 192, 186, 167, 151, 159], 
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Grouping data by 'school_code' and calculating mean, min, and max for 'age'
school_age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Plotting horizontal bar chart for mean, min, and max age per school
school_age_stats.plot(kind='barh', figsize=(8, 6), color=['skyblue', 'lightgreen', 'salmon'])

# Adding chart details
plt.title("Age Statistics by School Code")
plt.xlabel("Age")
plt.ylabel("School Code")
plt.tight_layout()

# Show the plot
plt.show()
