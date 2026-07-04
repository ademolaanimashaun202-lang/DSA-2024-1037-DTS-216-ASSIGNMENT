"""
DTS 216 - Question 7: Object-Oriented Programming
Create a class Student with attributes: Name, Matric Number, Department,
Level, CGPA. Methods: display_information(), calculate_class().
Create five student objects.
"""


class Student:
    def __init__(self, name, matric_number, department, level, cgpa):
        self.name = name
        self.matric_number = matric_number
        self.department = department
        self.level = level
        self.cgpa = cgpa

    def calculate_class(self):
        """Return the degree classification based on CGPA."""
        if 4.50 <= self.cgpa <= 5.00:
            return "First Class"
        elif 3.50 <= self.cgpa <= 4.49:
            return "Second Class Upper"
        elif 2.40 <= self.cgpa <= 3.49:
            return "Second Class Lower"
        elif 1.50 <= self.cgpa <= 2.39:
            return "Third Class"
        else:
            return "Pass"

    def display_information(self):
        print("-" * 40)
        print(f"Name:            {self.name}")
        print(f"Matric Number:   {self.matric_number}")
        print(f"Department:      {self.department}")
        print(f"Level:           {self.level}")
        print(f"CGPA:            {self.cgpa}")
        print(f"Class of Degree: {self.calculate_class()}")


if __name__ == "__main__":
    students = [
        Student("Animashaun Ademola Solomon", "DSA/2024/1037", "Data Science", "200", 4.72),
        Student("Chinedu Okoro", "SCI/2022/018", "Computer Science", "300", 3.85),
        Student("Amaka Johnson", "SCI/2021/102", "Statistics", "400", 2.95),
        Student("Bello Yusuf", "SCI/2023/077", "Data Science", "100", 1.98),
        Student("Grace Adeyemi", "SCI/2020/044", "Mathematics", "400", 1.20),
    ]

    print("=== Student Records ===")
    for student in students:
        student.display_information()
    print("-" * 40)
