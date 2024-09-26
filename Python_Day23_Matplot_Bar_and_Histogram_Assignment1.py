#Create a bar chart to represent monthly expenses in different spending categories and give your conclusion.

#Importing matplotlib library for plotting
import matplotlib.pyplot as plt
#Input Categories & Expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]
#Creating a bar chart using the categories and expenses data
plt.bar(categories,expenses, width=0.4)
#Adding a label for the x-axis
plt.xlabel("Categories")
#Adding a label for the y-axis
plt.ylabel("Expenses")
#Adding a title for the chart
plt.title("Monthly Expenses")
#Displaying the chart
plt.show()
