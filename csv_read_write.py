import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [85, 92, 78]
})

df.to_csv("students.csv", index=False)

loaded_df = pd.read_csv("students.csv")

print("Data read from CSV:")
print(loaded_df)
