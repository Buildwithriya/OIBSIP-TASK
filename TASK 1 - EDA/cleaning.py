import pandas as pd 

df=pd.read_csv(r"C:\Users\Riya\OneDrive\Documents\OIBSIP\TASK 1 - EDA\retail_sales_dataset.csv")

# initial inspection 

df.info() # getting the info of the dataset

print(df.isnull().sum())  # checking of null values 

print(df.head())


print(df.describe()) # statistical summary 

