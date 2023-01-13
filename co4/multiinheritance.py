class student:
    "information adndcs"
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("RollNo=",self.roll)
        print("student name=",self.name)
        print("course=",self.course)
class Mark:
    def __init__(self,mark):
        self.mark=mark
class details(student,mark):
    def __init__(self,roll,name,course,mark,hostelflag):
        student.__init__(self,roll,name,course)
        Mark.__init__(self,mark)
        self.hostelflag=hostelflag
    def displaydetails(self):
        self.display()
        print("Mark=",self.mark)
        print("hostel=",self.hostelflag)
s1=details(475,"Karthik","B.ed",789,True)
s1.displaydetails()
