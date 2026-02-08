with open('delicious/test2.txt','r') as file:
    content=file.read()
    print(content)
# readlines() method: returns list of strings, one per line
with open('romeo.txt','r') as short_file:
    s_content=short_file.readlines()  # Returns list with each line as a string
    print(s_content)
#You can also iterate through the file line by line:
for line in s_content:
    print(line)

#writing to files
"""with open('test.txt','w') as test3_file:
    test3_file.write('Hello World \n')"""
# Append to file: 'a' mode appends to existing file
with open('test.txt', 'a') as test:  # 'a' = append mode
    test.write('\n Bacon is not a vegetable.')
