from typing import List

class Student:
    def __init__(self, name: str, grade: int) -> None:
        """
        Initialize a Student instance.

        :param name: Student's name
        :param grade: Student's grade (integer)
        """
        self.name: str = name
        self.grade: int = grade

    def display(self) -> None:
        """Print a friendly message about the student."""
        print(f"{self.name} is in grade {self.grade}")


def main() -> None:
    # Example objects
    s1 = Student("Alice", 8)
    s2 = Student("Bob", 7)

    # Call display on each
    s1.display()   # Alice is in grade 8
    s2.display()   # Bob is in grade 7

    # Demonstrate working with a collection of students
    students: List[Student] = [s1, s2, Student("Charlie", 9)]
    print("\nAll students:")
    for s in students:
        s.display()

    # Example: compute average grade
    avg = sum(s.grade for s in students) / len(students)
    print(f"\nAverage grade: {avg:.2f}")


if __name__ == "__main__":
    main()
