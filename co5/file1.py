fr=open("sample.txt","r")
fw=open("s.txt","w")
for line in fr.readlines():
    fw.write(line)
fr.close()
fw.close()
fw1=open("s.txt","r")
for line in fw1.readlines():
    print(line)
fw1.close()
