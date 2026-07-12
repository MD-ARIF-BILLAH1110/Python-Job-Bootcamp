student_result = {
    "name": input("Enter Name: "),
    "bangla": int(input("Enter Bangla Marks: ")),
    "english": int(input("Enter English Marks: ")),
    "math": int(input("Enter Math Marks: "))
}

print("-------Result--------\n")
print(f"Name: {student_result['name']}")
print(f"Bangla: {student_result['bangla']}")
print(f"English: {student_result['english']}")
print(f"Math: {student_result['math']}")

total = student_result["bangla"] + student_result["english"] + student_result["math"]
print(f"\nTotal: {total}")
print(f"Average: {total / 3}")