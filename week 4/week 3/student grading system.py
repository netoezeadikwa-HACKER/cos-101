print("                      CHECK YOUR RESULTS HERE")

student_name = input("Enter the Students Name: ")
score = float(input("Enter the score from 0 - 100: "))

if score < 0 or score > 100:
    print("Invalid score. Score must be between 0 and 100")
else:
    if score >= 95:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"

    print()
    print()
    print("STUDENT RESULT")
    print("==============")
    print(f"Name: {student_name}")
    print(f"Score: {score:.2f}")
    print(f"Grade: {grade}")



























