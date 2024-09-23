#Calculate the profit made by a company

#Import numpy library
import numpy as np

#Input the revenue and expenses
revenue = np.array([10000, 12000, 11000, 10500])

expenses = np.array([4000, 5000, 4500, 4800])

#Calculate profit using "-"
Profit = revenue - expenses

#Display The Profit
print("Profit made by the company: ")
print(Profit)

#Output
'''
Profit made by the company: 
[6000 7000 6500 5700]
'''
