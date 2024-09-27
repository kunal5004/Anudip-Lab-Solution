#Create a pie chart to visualize the distribution of your monthly income by source. You have collected data on the various sources of your income, such as salary, freelance work, investments, and rental income.
#Share your conclusion/analysis.

#import matplotlib library
import matplotlib.pyplot as plt
#Income sources Data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other'] 

monthly_income = [5000, 1500, 1000, 600, 400]
#colors for slices of piechart
colors=['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightgrey']
#plotting the pie chart
plt.pie(monthly_income, labels=income_sources, colors=colors, autopct='%1.1f%%')
#provide title
plt.title("Distribution of monthly income")
#Display the pie chart
plt.show()
