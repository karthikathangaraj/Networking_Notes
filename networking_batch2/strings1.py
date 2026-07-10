name="karthika"
easy='''

this
is 
a demo
for more
then 
1
line
'''
print(easy) 
l1=list(name)
print(l1)
print(name[1:5:2])



s = "Python"

print("Py" in s)

print("Java" in s)

print("Java" not in s)

print(len(easy))
print(chr(65))
print(chr(107))
# A-65 +25=A-Z
# a-97 a-z
print(ord('a')) 

print("karthika\tthangaraj")
print("karthika\nthangaraj") 

name="karthika"
city="chennai"
print(f"i am {name} i am from {city}")
s = "Python Programming"

print(s.upper())

print(s.lower())

print(s.title())

print(s.capitalize())

print(s.swapcase())

print(s.casefold())

# s = "Straße"

# print(s.lower())
# print(s.casefold())

print(s.find("Pro"))

print(s.index("Pro"))

print(s.count("m"))

print(s.startswith("Py"))

print(s.endswith("ing"))

s="anitha,vanitha,monika"
print(s.split(",")) 
print(s.replace('anitha',"karthika")) 
s = "this   Python   " 
print(s.rstrip()) 
print("abc".isalpha())
print("123".isdigit())
print("abc123".isalnum())
print("python".islower())
print("PYTHON".isupper())
print("Hello".istitle())
print("   ".isspace())