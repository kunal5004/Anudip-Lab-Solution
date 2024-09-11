#Write a Python script to concatenate the following dictionaries to create a new one. 

#Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

#Concatenating the dictionaries
result_dict = {**dic1, **dic2, **dic3} #** extracts or "unpacks" the key-value pairs from that dictionary.
#The curly braces {} create a new dictionary,

#Print the result
print(f"Concatenated Dictionary: {result_dict}")


#Output
#Concatenated Dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
