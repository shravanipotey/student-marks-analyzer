students = {
    "Asha": 82,
    "Ravi": 67,
    "Meena": 91,
    "Kiran": 45,
    "Sneha": 74,
}

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

total = 0
for name, marks in students.items():
    print(f"{name}: {marks} -> Grade {get_grade(marks)}")
    total += marks

average = total / len(students)
highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print(f"\nClass average: {average:.2f}")
print(f"Highest: {highest} ({students[highest]})")
print(f"Lowest: {lowest} ({students[lowest]})")