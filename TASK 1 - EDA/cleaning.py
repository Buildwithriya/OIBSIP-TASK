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
                        bins=[17,25,35,45,55,65],
                        labels=['18-24', '25-34', '35-44', '45-54', '55-64'])
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
# monthly = monthly[monthly['Month_str'] < '2024-01']
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
# chart1 : monthly revenue 
plt.figure(figsize=(12,6))
sns.lineplot(data=monthly, x='Month_str', y='Total Amount', marker='o',color='blue',linewidth=2.5)
plt.title('Monthly Revenue Trend',fontsize=18,fontweight='bold',color='darkblue',pad=20)
plt.xlabel('Month', fontsize=14,fontweight='bold',color='darkblue')
plt.ylabel('Total Revenue', fontsize=14,fontweight='bold',color='darkblue')

for i, row in monthly.iterrows():
    plt.text(row['Month_str'], row['Total Amount'] + 1000, f"₨ {int(row['Total Amount']):,}", 
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.ylim(0, monthly['Total Amount'].max() * 1.2)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# chart 2: month over month change
plt.figure(figsize=(12,6))
sns.barplot(data=monthly, x='Month_str', y='MOM_Change', color='orange', edgecolor='black')
plt.title('Month-over-Month Revenue Change (%)', fontsize=18, fontweight='bold', color='darkblue', pad=20)
plt.xlabel('Month', fontsize=14, fontweight='bold', color='darkblue')
plt.ylabel('MoM Change (%)', fontsize=14, fontweight='bold', color='darkblue')
for i, row in monthly.iterrows():
    plt.text(row['Month_str'], row['MOM_Change'] + 0.5, f"{row['MOM_Change']:.1f}%", 
             ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# chart 3 : revenue by category
plt.figure(figsize=(12,6))
sns.barplot(data=cat_analysis , x='Product Category', y='total_revenue',linewidth=2, edgecolor='black',palette='viridis', 
    hue='Product Category',  legend=False)
plt.title('Revenue by Product Category', fontsize=18, fontweight='bold', color='darkblue', pad=20)
plt.xlabel('Product Category', fontsize=14, fontweight='bold', color='darkblue')
plt.ylabel('Total Revenue', fontsize=14, fontweight='bold', color='darkblue')

for i, row in cat_analysis.iterrows():
    plt.text(i, row['total_revenue'] + 1000, f"₨ {int(row['total_revenue']):,}", 
             ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.ylim(0, cat_analysis['total_revenue'].max() * 1.2)

plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# chart 4: gender breakdown
plt.figure(figsize=(8,6))
sns.barplot(data=gender_cat, x=gender_cat.index, y='Total Amount', color='lightcoral', edgecolor='black')
plt.title('Revenue by Gender', fontsize=18, fontweight='bold', color='darkblue', pad=20)
for i , row in gender_cat.iterrows():
    plt.text(i, row['Total Amount'] + 1000, f"{int(row['Total Amount']):,}", 
             ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.xlabel('Gender', fontsize=14, fontweight='bold', color='darkblue')
plt.ylabel('Total Revenue', fontsize=14, fontweight='bold', color='darkblue')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# chart 5: age group analysis
plt.figure(figsize=(12,6))
sns.barplot(data=age_group_analysis.reset_index(), x='Age_Group', y='Total', color='lightgreen', edgecolor='black')
plt.title('Revenue by Age Group', fontsize=18, fontweight='bold', color='darkblue', pad=20)
for i, row in age_group_analysis.reset_index().iterrows():
    plt.text(i, row['Total'] + 1000, f"₨ {int(row['Total']):,}", 
             ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.xlabel('Age Group', fontsize=14, fontweight='bold', color='darkblue')
plt.ylabel('Total Revenue', fontsize=14, fontweight='bold', color='darkblue')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# chart 6: top 10 customers

plt.figure(figsize=(12,6))
sns.barplot(x=top_customers.index, y=top_customers.values, color='skyblue', edgecolor='black')
plt.title('Top 10 Customers by Total Revenue', fontsize=18, fontweight='bold', color='darkblue', pad=20)
for i, value in enumerate(top_customers.values):
    plt.text(i, value , f"₨ {int(value):,}", 
             ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.xlabel('Customer ID', fontsize=14, fontweight='bold', color='darkblue')
plt.ylabel('Total Revenue', fontsize=14, fontweight='bold', color='darkblue')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()