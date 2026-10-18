import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Neha"],
    "Marks": [85, 92, 58, 76]
})

result = df.sort_values(
    by="Marks",
    ascending=False
)

print(result)
