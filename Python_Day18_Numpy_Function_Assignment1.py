#Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions.
#Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day).

#Importing the numpy library
import numpy as np
#Input Temperatures
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12])
#Find indices of temperatures greater than 35 (hot days)
hot=np.where(temperatures>35)
#Find indices of temperatures less than 5 (cold days)
cold=np.where(temperatures<5)
#Display the hot days
print("Hot Days: ")
print("Day\tTemperature (°C)")
#Iterate over the indices of hot days and print day number and temperature
for index in hot[0]:
#Using index+1 to represent day number
    print(f"{index+1}\t{temperatures[index]:.1f}")
#Display the Cold days
print("\nCold Days: ")
#Iterate over the indices of cold days and print day number and temperature
print("Day\tTemperature (°C)")
for index in cold[0]:
#Using index+1 to represent day number
    print(f"{index+1}\t{temperatures[index]:.1f}")

#Output
'''
Hot Days: 
Day	Temperature (°C)
3	36.8
6	38.7
10	37.2

Cold Days: 
Day	Temperature (°C)
11	-4.0
12	-12.0
'''
