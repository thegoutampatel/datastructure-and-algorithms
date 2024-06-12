
#Methods are the Function

class Student:
    college_name = "Patel College" 

    def __init__(self,name, marks):
        self.name = name   #Object Atrribute
        self.marks = marks
        print("Student Data Stored Succesfull")

    #These are the Methods
    def Welcome(self):
        print("Welcome Students")

    def hello(self):
        print("Hello Student," , self.name)

    def get_marks(self):
        return self.marks


s1 = Student("Goutam", 77)
print(s1.name, s1.marks)
s1.Welcome()
s1.hello()
print(s1.get_marks())
