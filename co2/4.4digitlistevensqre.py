from math import sqrt

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
perfectsqr=[]

for n in range(start, end):
    if (int(sqrt(n)) * int(sqrt(n))) == n:
        perfectsqr.append(n)


sqreven = [n for n in perfectsqr if all(int(a) % 2 == 0 for a in str(n))]

print(sqreven)
        
