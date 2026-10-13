import pandas as pd

data = {
    "RollNo": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Rohan", "Kavya", "Arjun", "Simran"],
    "Department": ["BCA", "BCA", "MCA", "BCA", "MCA", "MCA", "BCA", "MCA"],
    "Age": [20, 21, 22, 20, 23, 22, 21, 24],
    "Marks": [85, 92, 67, 78, 88, 95, 55, 73],
}
df = pd.DataFrame(data)

# Lab Sheet 2 - Q26
def grade(mark):\n    if mark >= 90: return "A+"\n    if mark >= 80: return "A"\n    if mark >= 70: return "B"\n    if mark >= 60: return "C"\n    return "D"\ndf["Grade"] = df["Marks"].apply(grade)\nprint(df[["Name", "Marks", "Grade"]])
