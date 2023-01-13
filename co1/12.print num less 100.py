n=4
l=[]
for i in range(n):

    d=int(input("Numbers="))
    if(d<=100):
        l.append(d)
    else:
        l.append("over")
print(l)        
