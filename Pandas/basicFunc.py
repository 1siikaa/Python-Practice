import pandas as pd

df = pd.DataFrame({
    "name": ["subh", "lubh", "tubh"],
    "age": [20, 50, 80],
    "salaries": [10000, 50000, 20000]
})
# loc is used to select data from a DataFrame using names (labels).
print(df.loc[df["age"] > 30, ["name", "salaries", "age"]])
print(df.loc[1])
print(df.loc[:, ["age", "salaries"]])
# : means all rows
print(df.loc[0:1, ["name", "age"]])
# loc includes the end index (0:1 includes 1)
df.loc[df["age"] > 30, "salaries"] = 45000
print(df)
print(df["age"]) # good for reading only not for complex updates
print(df.at[1, "age"])
print(df.iat[1, 2]) # single value, faster

# iloc is used to select data by position (numbers), not names.
print(df.iloc[1])
print(df.iloc[1, 2])
print(df.iloc[:])
print(df.iloc[1:3])
print([df.iloc[0:3, 0:3]])
print([df.iloc[:, :]])
print(df.iloc[[0,2], [0,2]])
df.iloc[1, 1] = 70
print([df.iloc[1]])
print(df.iloc[-1]) # last row
print(df.iloc[:, -1]) # last column
df["tax"] = df["salaries"] * 0.1 # create new column
print(df)
print(df.sort_values(by="salaries"))
print(df.sort_values(by="salaries", ascending=False))
# multiple condition
print(df[(df["age"]>30) & (df["salaries"] < 50000)]) # and
print(df[(df["age"]>30) | (df["salaries"] < 50000)]) # or


	# 1.	Create DataFrame with name, age, salary
df1 = pd.DataFrame({
  "name": ["aaa", "bbb", "ccc"],
  "age": [11, 22, 36],
  "salary": [11111, 22222, 53333]
})
print(df1)
	# 2.	Select first 3 rows using iloc
print(df1.iloc[:])
print(df1.iloc[:, 0])
	# 3.	Select rows where age > 30 using loc
print(df1.loc[df1["age"] > 30])
	# 4.	Filter salary between 50k and 70k
print(df1[(df1["salary"] > 50000) & (df1["salary"] < 70000)])
	# 5.	Add bonus column (10% salary)
df1["bonus"] = df1["salary"] * 0.1
print(df1)
	# 6.	Increase salary for age > 35
df1.loc[df1["age"] > 35, "salary"] += 500
print(df1)
	# 7.	Sort by age descending
print(df1.sort_values(by="age", ascending=False))
	# 8.	Select only name & salary columns
print(df1.iloc[[0,2], [0,2]])
	# 9.	Find shape of DataFrame
print(df1.shape)
	# 10.	Get max salary value
print(df1["salary"].max())