#Calculate the total revenue generated by two product categories in a store 

#Import numpy Library
import numpy as np

#input Revenues
category1_revenue = np.array([500, 600, 700, 550])

category2_revenue = np.array([450, 700, 800, 600])

#Add Both the revenue using +
Total_revenue=category1_revenue+category2_revenue

#Display The Addition
print("Total Revenue Generated:")

print(Total_revenue)

#Output
'''
Total Revenue Generated:
[ 950 1300 1500 1150]
'''
