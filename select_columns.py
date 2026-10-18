import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [85, 92, 78],
    "Age": [20, 21, 19]
})

print("Names:")
print(df["Name"])

print("\nNames and Marks:")
print(df[["Name", "Marks"]])
