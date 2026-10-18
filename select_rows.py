import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [85, 92, 78]
})

print("First row:")
print(df.iloc[0])

print("\nFirst two rows:")
print(df.iloc[0:2])
