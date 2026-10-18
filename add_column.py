import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [85, 92, 58]
})

df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

print(df)
