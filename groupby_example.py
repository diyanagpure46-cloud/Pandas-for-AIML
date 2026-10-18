import pandas as pd

df = pd.DataFrame({
    "Department": ["AIML", "CSE", "AIML", "CSE"],
    "Marks": [85, 78, 95, 88]
})

result = df.groupby("Department")["Marks"].mean()

print("Average marks by department:")
print(result)
