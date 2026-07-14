import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

df=pd.read_csv('shopping_trends.csv')
print(df) 
print(df.head())
print(df.drop)
print(df.dropna)
print(df.describe)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

#Age Distribution (Histogram)
plt.hist(df['Age'],bins=10)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show() 

#Category-wise Sales (Bar Chart)
sales= df.groupby('Category')['Purchase Amount (USD)'].sum()
sales .plot(kind='bar')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show() 

#Season-wise Sales (Bar Chart)
season = df.groupby('Season')['Purchase Amount (USD)'].sum()
season.plot(kind='bar')
plt.title('Sales by Season')
plt.ylabel('Total Sales')
plt.show() 

#Line Chart (Season-wise Average Purchase Amount)
season_sales = df.groupby("Season")["Purchase Amount (USD)"].mean()
season_sales = season_sales.reindex(["Spring", "Summer", "Fall", "Winter"])
plt.figure(figsize=(8,5))
plt.plot(season_sales.index,
         season_sales.values,
         marker='o',
         linewidth=2)
plt.title("Average Purchase Amount by Season")
plt.xlabel("Season")
plt.ylabel("Average Purchase Amount (USD)")
plt.grid(True)
plt.show() 

#Simple Heat Map
numeric_df = df.select_dtypes(include=["int64","float64"])
corr = numeric_df.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr,
            annot=True,
            cmap="coolwarm")

plt.title("Correlation Heat Map")
plt.show() 