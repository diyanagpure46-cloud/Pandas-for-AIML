import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [85, None, 75]
})

print("Missing values:")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)

print("\nAfter filling missing values:")
print(df)
