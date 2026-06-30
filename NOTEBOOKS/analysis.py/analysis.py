import pandas as pd

# Load dataset
df = pd.read_csv("DATA/SampleSuperstore.csv")

# Display first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Information:\n")
df.info()