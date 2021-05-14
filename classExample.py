class Student:
    def __init__(self, age, name, grade):
        self.name = name
        self.grade = grade
        self.age = age

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max__students):
        self.name = name;
        self.max__students = max__students;
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max__students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        # print(self.students)
        value = 0
        for student in self.students:
            # The "student" here is an entry of a list containing the object of the previous class that is Student
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)

print(course.get_average_grade())
