"""
DTS 216 - Question 1a
Program to classify a student's average score (from 5 courses) into a grade
using if-elif-else statements.
"""

def get_score(course_number):
    """Prompt the user for a single course score and return it as a float."""
    score = float(input(f"Enter score for course {course_number}: "))
    return score


def calculate_grade(average):
    """Return the letter grade for a given average score."""
    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 45:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"
    return grade


def main():
    print("=== Student Grade Classifier (5 courses) ===")
    scores = []
    for i in range(1, 6):
        scores.append(get_score(i))

    average = sum(scores) / len(scores)
    grade = calculate_grade(average)

    print("\n--- RESULT ---")
    for i, s in enumerate(scores, start=1):
        print(f"Course {i} score: {s}")
    print(f"Average score: {average:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
