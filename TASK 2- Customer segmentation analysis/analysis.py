

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

Q1 = df['MntTotal'].quantile(0.25)
Q3 = df['MntTotal'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['MntTotal'] < lower_bound) | (df['MntTotal'] > upper_bound)]
print(outliers.head())

data = df[(df['MntTotal'] > lower_bound) & (df['MntTotal'] < upper_bound)]
print(data.describe())

# box plot histogram for income
plt.figure(figsize=(6, 4))
sns.boxplot(data=df,y='Income',color='yellow')
for i in range(0, len(df['Income']), 100):
    plt.text(i, df['Income'][i], str(df['Income'][i]), fontsize=8, ha='center', va='bottom')
plt.title('Box Plot for Income')
plt.ylabel('Income')
plt.show()


# histogram for age
plt.figure(figsize=(6,4))
sns.histplot(data=df,x='Age',bins=20,color='brown',kde=True)
plt.title('Histogram for Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


print("Skewness: %f" % data['Age'].skew())
print("Kurtosis: %f" % data['Age'].kurt())


# corelation matrix
cols_demographics = ['Income','Age']
cols_children = ['Kidhome', 'Teenhome']
cols_marital = ['marital_Divorced', 'marital_Married','marital_Single', 'marital_Together', 'marital_Widow']
cols_mnt = ['MntTotal', 'MntRegularProds','MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
cols_communication = ['Complain', 'Response', 'Customer_Days']
cols_campaigns = ['AcceptedCmpOverall', 'AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
cols_source_of_purchase = ['NumDealsPurchases', 'NumWebPurchases','NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth']
cols_education = ['education_2n Cycle', 'education_Basic', 'education_Graduation', 'education_Master', 'education_PhD']

corr_matrix = data[['MntTotal']+cols_demographics +cols_children].corr()
plt.figure(figsize=(6,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


# k means clustering 