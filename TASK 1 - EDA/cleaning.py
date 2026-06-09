import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\Riya\OneDrive\Documents\OIBSIP\TASK 1 - EDA\retail_sales_dataset.csv")

# initial inspection 

print(df.shape)
df.info() # getting the info of the dataset


print(df.head())


# fix the datatype
df['Date']= pd.to_datetime(df['Date'])
print(df.dtypes)

# checking for missing / duplicate value
print(df.isnull().sum())  # checking of null values 
print(df.duplicated().sum()) # duplicated values

# creating new column for month and quarter
df['Year']=df['Date'].dt.to_period('Y')

df['Month']=df['Date'].dt.to_period('M')
df['Quarter']= df['Date'].dt.to_period('Q')

df['Age_Group']=pd.cut(
                        df['Age'],
                        bins=[17,25,35,45,55,65,75],
                        labels=['18-24', '25-34', '35-44', '45-54', '55-64', '65-74'])
print(df.head())


# descriptive statistics
print(df[['Age', 'Quantity', 'Price per Unit', 'Total Amount']].describe().round(2))

# count by category
print(df['Product Category'].value_counts())

print(df.groupby('Product Category')['Total Amount'].sum())

# time series analysis 
# monthly total revenue
monthly = df.groupby('Month')['Total Amount'].sum().reset_index()

monthly['Month_str'] = monthly['Month'].astype(str)
monthly = monthly[monthly['Month_str'] < '2024-01']
print(monthly)


# month over month % change 

monthly['MOM_Change']= monthly['Total Amount'].pct_change()*100

print(monthly[['Month_str','Total Amount','MOM_Change']].round(2))

# customer and product analysis
#  revenue by category
cat_analysis=df.groupby('Product Category')['Total Amount'].agg(total_revenue='sum',
                                                                avg_transaction='mean',
                                                                Num_transaction='count').round(1)
print(cat_analysis)

# gender breakdown 
print(df.groupby('Gender')['Total Amount'].sum())
gender_cat=df.pivot_table(index='Gender', values='Total Amount', aggfunc='sum')
print(gender_cat)

# age group analysis
age_group_analysis= df.groupby('Age_Group', observed=True)['Total Amount'].agg(
    Total='sum',
    Average='mean',
    Count='count'
).round(1)
print(age_group_analysis)

# top 10 customers

top_customers=df.groupby('Customer ID')['Total Amount'].sum().nlargest(10)
print(top_customers)

# visualization