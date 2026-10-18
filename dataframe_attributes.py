import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [85, 92, 78]
})

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Number of rows:", len(df))
print("Data types:")
print(df.dtypes)
