str="RahulShettyAcademy.com"

print(str[1])
str1="Consulting Firm"
str2="rahulshetty"
print(str[0:5]) #substring
print(str+str1) #concatenation
print(str2 in str) #substring check so it will return true or false
var=str.split(".") #two substrings will be there in output
print(var)
str3=" great "  #for removing whitespaces
print(str3.rstrip())
print(str3.lstrip())
print(str3.strip())
print(str2.capitalize()) #only first letter is capitalize
str4=str1.replace("Firm","Law")
print(str4)
print(str.upper()) #all chars in upper case
print(str.lower())
print(str.center(150,'-'))#for aligning string str.center(width[, fillchar])
sentence = "python is easy and python is powerful"
print(sentence.count("python")) #is used to count how many times a substring appears in a string
print(str.endswith(".com")) #returns true or false
text = "bananaaaaanaaa123"
print(text.count("a", 1, 15))
print(text.isascii())
print(text.isnumeric())
print(text.isalnum()) #alphabet and numbers
print(text.isprintable()) #not containing \n or \t
#conversts a string into byte
encoded = text.encode("utf-8")
print(encoded)
x = "Hello\tWorld"
print(x.expandtabs(4))
y = "automation testing"
print(y.find("testing")) #first occurrence of substring position
name = "Nikita"
role = "QA Engineer"

print("My name is {} and I am a {}".format(name, role))
payload = {
    "status": "PASS",
    "module": "Login"
}

log = "Module {module} execution {status}".format_map(payload)
print(log)




