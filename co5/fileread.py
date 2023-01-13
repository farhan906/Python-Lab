s="Hello All"
with open("filereed.txt","w") as f:
    f.write(s)
with open("filereed.txt","r") as fr:
    print(fr.read())
