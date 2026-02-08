#Get method for dictionary for checking if key value pairs is alreadythere in dict
# and assessing a default value if key is not there
#sender which is used max times in the file
fhand=open('mbox-short.txt')
counts=dict()
for line in fhand:
    line=line.rstrip() #to remove that extra line
    if line.startswith('From '):
        words = line.split()
        email= words[1].strip()
        #print(email)
        counts[email] = counts.get(email, 0) + 1
max_email = None
max_count = None
for email, count in counts.items():
    print(email,count)
    if max_count is None or count > max_count:
        max_email = email
        max_count = count
print("this email is :",max_email, max_count)
