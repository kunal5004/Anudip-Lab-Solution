# Write a Pandas program to create a dataframe from a dictionary and display it.
#Import Pandas library
import pandas as pd
#Input Colums and values
score={'Math':[78,85,96,80,86], 'English':[84,94,89,83,86],'Hindi':[86,97,96,72,83]} 
#Creating DataFrame
df=pd.DataFrame(score)
#Display DataFrame
print(df)

#Output
'''
   Math  English  Hindi
0    78       84     86
1    85       94     97
2    96       89     96
3    80       83     72
4    86       86     83
'''
