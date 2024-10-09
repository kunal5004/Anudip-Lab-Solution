#Write a Pandas program to create a Pivot table and find the item wise unit sold.

#Importing Pandas Library
import pandas as pd

# Load the sales data from CSV file
sales_data = pd.read_csv(r"C:\Users\Kunal\Downloads\salesdata.csv")

# Display the first few rows of the dataset to understand its structure
print(sales_data.head())

# Create a Pivot Table to calculate item-wise units sold
pivot_table = pd.pivot_table(sales_data, 
                             values='Units',  # Correct column for units sold
                             index='Item',  # Correct column for item
                             aggfunc='sum')

# Display the Pivot Table
print(pivot_table)

#Output
'''
    Region  Manager   SalesMan          Item  Units  Unit_price  Sale_amt
0     East   Martha  Alexander    Television     95      1198.0  113810.0
1  Central  Hermann     Shelli  Home Theater     50       500.0   25000.0
2  Central  Hermann       Luis    Television     36      1198.0   43128.0
3  Central  Timothy      David    Cell Phone     27       225.0    6075.0
4     West  Timothy    Stephen    Television     56      1198.0   67088.0
              Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395
'''
