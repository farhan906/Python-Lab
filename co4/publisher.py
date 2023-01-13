class publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        pass
class book(publisher):
    def __init__(self,name,title,author):
        self.name=name
        self.title=title
        self.author=author
    def display(self):
        pass

class python(book):
    def __init__(self,name,title,author,price,noPage):
        book.__init__(self,name,title,author)
        self.price=price
        self.noPage=noPage
    def display(self):
        print("publisher=",self.name)
        print("Title=",self.title)
        print("Author=",self.author)
        print("Price=",self.price)
        print("no of pages=",self.noPage)

p1=python("Doubleday (US)","DA VINCI CODE","Dan Brown",399,689)
p1.display()
        
