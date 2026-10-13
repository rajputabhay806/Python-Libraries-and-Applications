import pandas as pd

data = {
    "RollNo": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Rohan", "Kavya", "Arjun", "Simran"],
    "Department": ["BCA", "BCA", "MCA", "BCA", "MCA", "MCA", "BCA", "MCA"],
    "Age": [20, 21, 22, 20, 23, 22, 21, 24],
    "Marks": [85, 92, 67, 78, 88, 95, 55, 73],
}
df = pd.DataFrame(data)

# Challenge: build and export the final merit list.
def grade(mark):
    if mark >= 90: return "A+"
    if mark >= 80: return "A"
    if mark >= 70: return "B"
    if mark >= 60: return "C"
    return "D"

df["Grade"] = df["Marks"].apply(grade)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
df["Rank"] = df["Marks"].rank(ascending=False, method="min").astype(int)

merit_list = df[["Rank", "RollNo", "Name", "Department", "Marks", "Grade", "Result"]]
merit_list = merit_list.sort_values(["Marks", "RollNo"], ascending=[False, True])
merit_list.to_excel("student_merit_list.xlsx", index=False)
print(merit_list)
print("Saved student_merit_list.xlsx")
