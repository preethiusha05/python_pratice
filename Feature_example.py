def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

student_name = input("Enter student name: ")
marks = int(input("Enter marks (0–100): "))

grade = calculate_grade(marks)

print("\nStudent Report")
print("Name:", student_name)
print("Marks:", marks)
print("Grade:", grade)

