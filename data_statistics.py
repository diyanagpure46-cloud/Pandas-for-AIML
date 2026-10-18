import pandas as pd

df = pd.DataFrame({
    "Marks": [85, 92, 78, 65, 90]
})

print("Mean:", df["Marks"].mean())
print("Median:", df["Marks"].median())
print("Maximum:", df["Marks"].max())
print("Minimum:", df["Marks"].min())
print("\nSummary:")
print(df.describe())
