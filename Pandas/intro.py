# Pandas = Data Analysis Library

# It gives:
# 	•	Tables (like Excel / DB tables)
# 	•	Easy filtering, grouping, cleaning


import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
print(s.values)
print(s.index)
print(s.dtype)

prices = pd.Series([100, 200, 300], index=["apple", "banana", "orange"])
print(prices["orange"])


# pandas dataframe
# dictionary

data = {
    "name": ["john", "jacob", "dohn"],
    "salaries": [500, 600, 700],
    "department": ["HR", "OP", "IT"]
}

df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.columns)
print(df.values)
print(df.index)
print(df.shape)
print(df.dtypes)
print(df.ndim)
print(df.size)
print(df[df["department"] == "IT"])


# Pandas – 10 Questions
# 	1.	Create a Series from list [5,10,15]
list1 = [5, 10, 15]
s1 = pd.Series(list1)
print(s1)
# 	2.	Create Series with custom index
s2 = pd.Series([5, 10, 15], index=["pencil", "rubber", "cutter"])
print(s2)
# 	3.	Access element using index
print(s2["rubber"])
# 	4.	Create DataFrame with name & age
data1 = {
    "name": ["A", "B", "C"],
    "age": [2, 3, 4]
}
df1 = pd.DataFrame(data1)
print(df1)
# 	5.	Get column names
print(df1.columns)
# 	6.	Filter rows based on condition
print(df1[df1["age"]>3])
# 	7.	Add new column
df1["country"] = "India"
df1["isAdult"] = df1["age"] > 2
print(df1)
# 	8.	Update existing column
df1["age"] = df1["age"] + 10
print(df1)
df1.loc[df1["age"]>3, "age"] = df1["age"] + 20 # conditional update
print(df1)
# 	9.	Get DataFrame shape
print(df1.shape)
# 	10.	Select only one column
print(df1["name"]) # returns series
print(df1[["name"]]) # returns dataframe

#Solution
import pandas as pd

# 1. Create a Series from list [5, 10, 15]
s1 = pd.Series([5, 10, 15])
print(s1)

# 2. Create Series with custom index
s2 = pd.Series([5, 10, 15], index=["pencil", "rubber", "cutter"])
print(s2)

# 3. Access element using index
print(s2["rubber"])

# 4. Create DataFrame with name & age
df1 = pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [2, 3, 4]
})
print(df1)

# 5. Get column names
print(df1.columns)

# 6. Filter rows based on condition
print(df1[df1["age"] > 3])

# 7. Add new column
df1["isAdult"] = df1["age"] >= 3
print(df1)

# 8. Update existing column
df1["age"] = df1["age"] + 1
print(df1)

# 9. Get DataFrame shape
print(df1.shape)

# 10. Select only one column
print(df1["name"])