n=int(input("no of elements="))
dict={}
for i in range(n):
    key=int(input("enter the days="))
    value=str(input("enter the month="))

    dict[key]=value
print("acending order=",sorted(dict.items()))
print("decending order=",sorted((dict.items()),reverse=True))
