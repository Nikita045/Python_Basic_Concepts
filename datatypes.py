#different data types can be passed in list
a=[2,4,5.4,"nikita",[2.4,5,7]]

print(type(a))
print(len(a))
b=[2,7,19,1,0,23,100,6,9]
print(9 in b) #to check items in a list
b.sort()
print(b)#sort the list
#max, min, sum function in list
print(max(b))
print(min(b))
print(sum(b)/len(b))
print("**************************")
print(a[3])
print(a[-1]) #last value is printed
print(a[1:3])# 1 & 2 are included but 3 is not
print(a[:3])#excluding 3 all are included from 0 to 2
print(a[2:])
#insert value in the list in between
a.insert(4,"kataria")
print(a)
#append value in list at the end
a.append(1)
print(a)
#update values in a list
a[3]="Shivangi"
print(a)
#delete value from a list
del a[2]
print(a)

#Tuple are same as list but are immutable
val = (1,2,"hello",[5,4.3,"ok"])

print(type(val))
print(val)
print(val[2])

#Dictionary is an unordered sequence of data of key-value pair form.
dict={4:"first name",2:"last name","age":33}
print(type(dict))
print(dict)
print(dict[4]) #depends on key not on index
#empty dictionary
dict1={}
print(dict1)
dict1["first name"]="nikita"
dict1["last name"]="kataria"
dict1["age"]=28
print(dict1)

