class parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class child(parent):
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self):
        print(self.name)
        print(self.address)
obj=child("Rudhra","kollam")
obj.display()
