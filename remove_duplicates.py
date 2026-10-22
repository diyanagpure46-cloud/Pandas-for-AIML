import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Amit", "Rahul"],
    "Marks": [85, 92, 85, 78]
})

print("Original data:")
print(df)

result = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(result)
