import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("DATA/SampleSuperstore.csv")

# 1. Sales by Category
plt.figure(figsize=(8,5))
sns.barplot(x="Category", y="Sales", data=df)
plt.title("Sales by Category")
plt.show()

# 2. Profit by Category
plt.figure(figsize=(8,5))
sns.barplot(x="Category", y="Profit", data=df)
plt.title("Profit by Category")
plt.show()

# 3. Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=30)
plt.title("Sales Distribution")
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include="number").corr(),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()