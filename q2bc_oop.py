"""
DTS 216 - Question 2b, 2c
b. Class Student with attributes (name, roll_number, marks) and a method
   to calculate grade.
c. Subclass GraduateStudent (inheritance) with an additional attribute
   research_topic.
"""


class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_grade(self):
        """Return a letter grade based on the marks attribute."""
        if self.marks >= 70:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 50:
            return "C"
        elif self.marks >= 45:
            return "D"
        elif self.marks >= 40:
            return "E"
        else:
            return "F"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")


class GraduateStudent(Student):
    """Subclass of Student that adds a research_topic attribute."""

    def __init__(self, name, roll_number, marks, research_topic):
        super().__init__(name, roll_number, marks)
        self.research_topic = research_topic

    def display(self):
        super().display()
        print(f"Research Topic: {self.research_topic}")


if __name__ == "__main__":
    print("=== Undergraduate Student ===")
    s1 = Student("Chinedu Okoro", "SCI/2021/045", 78)
    s1.display()

    print("\n=== Graduate Student (Inheritance Demo) ===")
    g1 = GraduateStudent("Animashaun Ademola Solomon", "DSA/2024/1037", 82,
                          "Predictive Analytics using Machine Learning")
    g1.display()
