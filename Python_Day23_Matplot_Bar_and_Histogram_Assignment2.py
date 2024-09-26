#Visualize the daily temperature changes over time in a city and give your conclusion

#Import the matplotlib Library
import matplotlib.pyplot as plt
#Defining the days of the month 
days = list(range(1, 32))
#Defining the daily temperatures
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]
#Creating a line plot with markers at each data point
plt.plot(days,temperature,marker='o')
#Adding a label for the x-axis 
plt.xlabel("Days")
#Adding a label for the y-axis
plt.ylabel("Temperature")
#Adding a title for the chart
plt.title("Daily Temprature Changes")
#Displaying the chart
plt.show()
