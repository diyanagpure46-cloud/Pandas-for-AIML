import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [85, 92, 58],
    "Age": [20, 21, 19]
})

df = df.drop(columns=["Age"])

print(df)
