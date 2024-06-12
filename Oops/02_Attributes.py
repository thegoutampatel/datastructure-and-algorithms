
#Attributes
# -- Class Attr - For all the object class attributes is same and also stored only one
# -- Object Attr - This create diff attributes for diff Obj and stored diff memory

class Student:
    college_name = "Patel College"  #Class Attribute

    def __init__(self,name, marks):
        self.name = name   #Object Atrribute
        self.marks = marks
        print("Student Data Stored Succesfull")

s1 = Student("Goutam", 77)
print(s1.name, s1.marks)

#Both have same work
print(s1.college_name)
print(Student.college_name)