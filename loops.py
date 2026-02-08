greeting="Good Morning"

#code indentation is important in python
if greeting=="Morning":
    print("Condition Matched")
else:
    print("Condition Not Matched")
print("if else condition code is completed")
print("****************************")
#for loop
obj=[1,4.5,7,"hey","ok"]
for i in obj:
    print(i)
print("****************************")
#sum of first five natural nos 1+2+3+4+5=15
summation=0
for j in range(1,6):  #range i to j-1
    summation=summation+j
    #print(j)
print("total is ",summation)
print("****************************")
#if you want to increment i by 2 by default is 1
for k in range(1,10,2):
    print(k)
print("****************************")
#skipping first index
for m in range(10):
    print(m)
print("****************************")
#while loop -indefinite loop, you need to know when condition is false else loop will run infinite times
it=4
while it>1:
    if it!=3:
        print(it)
    it=it-1
print("****************************")
#break -halt the execution and continue means skipping current iteration
x=10
while x>1:
    if x==9:
        x=x-1
        continue  #infinite loop because it will always skip this 9th iteration and it's not going to decrement the value of x
    if x==3:
        break #halt the execution and come out of loop
    print(x)
    x=x-1
