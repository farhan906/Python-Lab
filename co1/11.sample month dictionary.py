dictionary={"jan":31,"feb":28,"mar":30,"apr":31}
print(dictionary)

month=input("enter the month=")
print("the number of days in month is",dictionary[month])

delete=input("enter the month to be deleted=")
dictionary.pop(delete)
print(delete,"removed")

key=input("enter the month to add to dictionary")
value=int(input("enter the number of days of month="))
dictionary[key]=value
s=sorted(dictionary.items()
print("sorted items",s)
