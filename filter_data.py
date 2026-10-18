import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Neha"],
    "Marks": [85, 92, 58, 76]
})

result = df[df["Marks"] >= 75]

print("Students scoring 75 or above:")
print(result)
