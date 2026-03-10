class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def greet(self):
        return f"Hello, my name is {self.firstname} {self.lastname}"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Student(Person):
    def __init__(self, firstname, lastname, student_id):
        super().__init__(firstname, lastname)
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{super().__str__()} (ID: {self.student_id})"


class Teacher(Person):
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        return [str(s) for s in self.students]

    def __str__(self):
        return f"{super().__str__()} - {self.subject}"


class Classroom:
    def __init__(self, name, teacher=None):
        self.name = name
        self.teacher = teacher
        self.students = []

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def enroll(self, student):
        self.students.append(student)

    def size(self):
        return len(self.students)

    def __str__(self):
        teacher_name = str(self.teacher) if self.teacher else "No teacher"
        return f"Classroom {self.name} | {teacher_name} | {self.size()} students"
