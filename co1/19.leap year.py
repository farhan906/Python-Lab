end=int(input("enter the final year="))
current=2022
while(end>=current):
        if end%4==0 and  end%100!=0:
            print(end)
        if end%100==0 and end%400==0:
            print(end)
        end=end-1
