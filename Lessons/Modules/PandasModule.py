import pandas as pd

data = [10, 20, 30, 40]
series = pd.Series(data)
print(series)


data_dict = {'a': 1, 'b': 2, 'c': 3}
series_dict = pd.Series(data_dict)
print(series_dict)

# From a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
print(df)


data2 = {
    "Product": ["Banana", "Apple", "Coconut"],
    "Price": [10.99, 25.99, 30.99],
    "Quantity": [1, 5, 3]
}

df2 = pd.DataFrame(data2)
#print(df2)

# Select a row by index
print(df.loc[0])  # Using label-based indexing
print(df.iloc[0])  # Using integer-based indexing

# Filter rows
filtered_df = df[df['Age'] > 30]
print(filtered_df)

df2["Column4"] = ["Value1", "Value2", "Value3"]
print(df2)

df.loc[df['Name'] == 'Alice', 'Age'] = 26
print(df)

# Drop a column
df = df.drop(columns=['Salary'])

# Drop a row
df = df.drop(index=1)
print(df)
