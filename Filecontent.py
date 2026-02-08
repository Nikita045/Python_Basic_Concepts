file=open('test.txt') #open file
#print(file.read())   # read file
#print(file.read(7))
#print(file.readline())
#print(file.readline())
#file.close()

#print line by line using readline method
#line=file.readline()
#while line!="":
 #   print(line)
   #line = file.readline()

#read line using for loop
for line in file.readlines():
    print(line)
file.close()