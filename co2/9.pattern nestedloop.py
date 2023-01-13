n=5
mid=int(n/2)
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end=" ")
    print()

for i in range(mid+2, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")

    print()