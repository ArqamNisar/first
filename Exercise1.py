import pandas as pd
import matplotlib.pyplot as plt

#importing data from csv file using pd.read_csv as a dataframe
#df = pd.read_csv(r"data.csv")

#printing the dataframe 
#df.head() 

#creating a pandas dataframe using python dictionaries
data = [{'a':1, 'b':2, 'c':3},{'a':5, 'b':10, 'c':20}]

df = pd.DataFrame(data)
df.head()

#using indexes
df1 = pd.DataFrame(data, index=['first','second'])
df1.head()

#%% Matplotlib Plot

plt.plot([1,2,3],[4,6,8])
plt.show()

#%%

import pandas as pd

df = pd.read_csv("C:/Users/jkhan.smme/Desktop/Pandas Exercises/data.csv")

print(df.to_string()) 

plt.plot(df)
plt.show()





