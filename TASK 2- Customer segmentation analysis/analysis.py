import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

print(df.describe())
# data explorationa and descriptive statistics

# total amount spent on products
print(df['MntTotal'].sum())
plt.figure(figsize=(6, 4))  
sns.boxplot(data=df, y='MntTotal')
plt.title('Box Plot for MntTotal')
for i in range(0, len(df['MntTotal']), 100):
    plt.text(i, df['MntTotal'][i], str(df['MntTotal'][i]), fontsize=8, ha='center', va='bottom')
plt.ylabel('MntTotal')
plt.show()