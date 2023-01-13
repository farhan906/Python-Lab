list1=[2,3,4,67,8,9]
list2=[3,88,55,6,5,0]
n=len(list1)
d=len(list2)
f=[]
if(n==d):
    print("same length")
else:
    print("diff length")



s=0
for i in list1:
    s=s+i
print("list1 sum=",s)
a=0
for i in list2:
    a=a+i
print("list2 sum=",a)
if(a==s):
    print("same sum")
else:
    print("diff sum")


comm=set(list1).intersection(list2)
f.append(comm)
print(f)




        
