my_list = [1, 2, 3, "Python", True]
#insertion
my_list.append(4)
print(my_list)
my_list.insert(1, 3.5)
print(my_list)
my_list.extend([4,"Rishi","nikki","riya",9,[3,45,"ravi",5.6]]) #inserts all these value at the end
print(my_list)
#remove
my_list.remove("Rishi") #removes a object
print(my_list)
my_list.pop()  #last item is popped out from a list
print(my_list)
my_list.pop(1) #index pop out
print(my_list)
my_list.clear() #clear all the values
print(my_list)

#arrange
lst=[1,4,67,2,7,0,5,2.6]
lst.sort()
print(lst)
lst.sort(reverse=True)  #reverse order
print(lst)
del lst[0]
print(lst)
lst.reverse()
print(lst)
print(lst.index(7)) #searches value 7 in list

my_lists = [1, "Python",2, 3, "Python", "Python",True]
print(my_lists.count("Python")) #counts how many times it came in list
#copy list
x=my_lists.copy()
print(x)

cube = [x*x*x for x in range(5)]
print(cube)
#to convert list to tuple
tuple_name = tuple(my_lists)
print(tuple_name)


#to convert back to list
list_name= list(tuple_name)
print(list_name)







