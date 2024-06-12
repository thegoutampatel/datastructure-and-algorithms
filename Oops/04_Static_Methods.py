# Static Method: Methods that don't use the self prameter 
#work at class level

class Student:

    def __init__(self,name, marks):
        self.name = name   #Object Atrribute
        self.marks = marks
        print("Student Data Stored Succesfull")
    
    @staticmethod  #decoretors
    def Welcome():
        print("Welcome Students")

s1 = Student("goutam",90)
#use Both
s1.Welcome()
Student.Welcome()