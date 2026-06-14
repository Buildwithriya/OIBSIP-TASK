import pandas as pd


# reading the dataset
df=pd.read_csv(r"C:\Users\Riya\OneDrive\Documents\OIBSIP\TASK 2- Customer segmentation analysis\ifood_df.csv")
# checking the first 5 rows of the dataset
print(df.head())

# checking the shape of the dataset
print(df.shape)
# checking the data types of the columns
print(df.dtypes)
print(df.info())
# checking for missing values
print(df.isnull().sum())
# checking for unique values
print(df.nunique())
# drop the columns which are not required for analysis
df.drop(['Z_CostContact','Z_Revenue'],inplace=True,axis=1)
print(df.info())