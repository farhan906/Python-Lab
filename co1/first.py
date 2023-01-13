
d={"JAN":31,"FEB":29,"MAR":31,"APR":30,"MAY":31}
m=input("Enter the number=")
print(d[m])
print(sorted(d.items(),reverse=True))
s=input("Enter the mont to be removed=")
del d[s]
print(d)

x=input("enter the monthe to add=")
insert(d[x])
d['JUN']=30
print(d)
