#Write a Python program and calculate the mean of the below dictionary.

test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
#Calculate the mean
mean= sum(test_dict.values()) / len(test_dict)
#Print the mean
print(f"The mean of the values of dictionary is {mean}")

#Output
#The mean of the values of dictionary is 6.2
