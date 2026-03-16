import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Joy", "Alex", "Faith"],
    "Age": [25, 30, 28],
    "City": ["Nairobi", "Mombasa", "Kisumu"]
}
df = pd.DataFrame(data)

# View data
print(df)

# Select a column
print(df["Name"])

# Filter rows
print(df[df["Age"] > 26])

# Basic stats
print(df["Age"].mean())
