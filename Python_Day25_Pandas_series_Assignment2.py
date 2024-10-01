#Suppose you want to track and analyze your household expenses for a month. You have recorded the expenses for various categories, such as groceries, utilities, rent, transportation, and entertainment.
#You can represent this expense data using a Pandas Series. 

#import panda library
import pandas as pd

#Data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]


#Creating series
expense_series=pd.Series(data=expenses,index=categories)
#Display series
print(expense_series)

#Output
'''
Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
dtype: int64
'''
