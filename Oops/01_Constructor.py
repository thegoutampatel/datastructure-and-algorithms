#Conctructor

class Student:
    #Default Constructor   --> created default by python
    def __init__(self):
        pass
    
    #Parametarized Contructor
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("Student Printed")

s1 = Student("Goutam", 77)
print(s1.name, s1.marks)

s2 = Student("Yogesh", 80)
print(s2.name, s2.marks)