import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('books_data.csv')

# Display first few rows
print(df.head())

# Remove '£' sign and convert to float
df['Price'] = df['Price'].str.replace('£', '').astype(float)

# Confirm changes
print(df.info())
print(df.describe())

avg_price = df['Price'].mean()
print(f"Average Book Price: £{avg_price:.2f}")

print("Top 5 Expensive Books:")
print(df.sort_values(by='Price', ascending=False).head())

print("Top 5 Cheapest Books:")
print(df.sort_values(by='Price').head())


#histogram

plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=10, kde=True, color='skyblue')
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Count")
plt.grid(True)
plt.show()

#cleaned_file
df.to_csv('cleaned_books_data.csv', index=False)