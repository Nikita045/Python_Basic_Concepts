fhand=open(input("Enter file name: "))  #taking input from user
#for multi line comment use """ """
count=0
for line in fhand:
    line=line.rstrip() #to remove that extra line
    if line.startswith('From:'): #this will print lines starting with From:
        #double split pattern
        count=count+1
        word=line.split(':')
        name=word[1].strip()
        sendername=name.split('@')
        print(sendername[0])
print("Total lines starting with From: are",count)

"""From: stephen.marquard@uct.ac.za
str ='From: stephen.marquard@uct.ac.za'
x=str.split('@')
name =x[0].split(':')
print(name[1].lstrip())"""
