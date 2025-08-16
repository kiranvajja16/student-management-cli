class Student:
    def __init__(self, roll_no, name, age, course,):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course

    def __repr__(self):
        return f"Student(Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Course: {self.course})"
