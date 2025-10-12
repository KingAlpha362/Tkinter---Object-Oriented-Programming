class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        
student = Student("Qaa-im", 20, "12345")
student.display_info()

        
    