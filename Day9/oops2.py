
class student:
    college_name = "ABC College"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    
    def display(self):
        print("Student name:",self.name)
        print("Student roll_no:",self.roll_no)
        
    @classmethod
    def change_college(cls,new_name):
        cls.college_name=new_name

student.change_college("XYZ College")
print(student.college_name)
s1=student("nisarga",2)
s1.display()

s2=student("nisa",3)
s2.display()