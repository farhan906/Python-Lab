class student:
    "information adndcs"
    def getdata(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("RollNo=",self.roll)
        print("student name=",self.name)
        print("course=",self.course)
class test(student):
    def getmark(self,mark):
        self.mark=mark
    def displaymarks(self):
        self.display
        print("mark=",self.mark)
s1=test()
s1.getdata(25,"Farhan","MCA")
s1.getmarks(736)
s1.displaymarks()
