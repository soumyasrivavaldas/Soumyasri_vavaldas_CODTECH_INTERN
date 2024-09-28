# Python Program to Track and Manage Student Grades
def calculate_average(grades):
    return sum(grades) / len(grades)
def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
def get_gpa(average):
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0
def grade_manager():
    print("Student Grade Manager")
    grades = []
    while True:
        grade_input = input("Enter a grade for the subject/assignment (or type 'done' to finish): ")
        if grade_input.lower() == 'done':
            break
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Please enter a valid grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    if len(grades) == 0:
        print("No grades were entered.")
        return
    average_grade = calculate_average(grades)
    letter_grade = get_letter_grade(average_grade)
    gpa = get_gpa(average_grade)
    print("\n===== Grade Report =====")
    print(f"Total Subjects/Assignments: {len(grades)}")
    print(f"Average Grade: {average_grade:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.1f}")
    print("========================")
grade_manager()
