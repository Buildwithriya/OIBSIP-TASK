import pandas as pd 

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

