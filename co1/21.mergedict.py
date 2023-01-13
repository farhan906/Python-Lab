d1={}
d2={}

n1=int(input("no of elements="))
for i in range(n1):
    key=input("enter the days=")
    value=input("enter the month=")
    
    d1[key]=value


n2=int(input("no of elements="))
for i in range(n2):
    key=input("enter the days=")
    value=input("enter the month=")
    
    d2[key]=value

print(d2.update(d1))
print("merged dictionary=",d2)
