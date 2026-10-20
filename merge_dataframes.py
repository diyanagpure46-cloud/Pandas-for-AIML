import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Priya", "Rahul"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [85, 92, 78]
})

result = pd.merge(students, marks, on="ID")

print(result)
