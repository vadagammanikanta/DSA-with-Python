from asyncio.windows_events import NULL
from operator import truediv

print("Hello World")

a=10
b=10.9
c=' Mani Kanta '
d="Manikanta"
words=["Mani","Kanta"]
e=False
f=[10,20,30,"Mani"]
g=(10,20,30,"Mani")
h={10,20,30,"Mani"}
j={"name":"mani","age":20}



print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))
print(g)
print(type(g))
print(h)
print(type(h))
print(j)
print(type(j))

#String Functions
print(d*3)
print(len(d))
print(d.lower())
print(d.upper())
print(c.strip())
print(c.lstrip())
print(c.rstrip())
print(d.replace('a','x'))
print(c.split())
print(" ".join(words))
print(c.find("a"))
print(c.find("x"))
print(d.index("M"))
print(d.count("a"))
print(d.startswith("Ma"))
print(d.endswith("ta"))
print(d.isalpha())
print(d.isnumeric())
print(d.isdigit())
print(d.isalnum())
print(d.isupper())
print(d.islower())
print(c.isspace())
print(d.isprintable())
print(d.capitalize())
print(c.title())
print(d.swapcase())
print(d.ljust(0))
print(d.rjust(0))
print(d.lstrip())
print(d.rstrip())
s="""Hi There,
I'm 
Manikanta"""
print(s)
print(type(s))
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(s)
print(s[0])
print(s[5])
print(s[-1])

#String Slicing
print(s[1:4])
print(s[0:-1])
print(s[:3])
print(s[::-1])#reverse method for strings in python
for char in s:
    print(char,end=" ")
print()
print(s)
del s
s = "ABCD EF"
s1 = "H" + s[1:]
s2 = s.replace("ABC", "abc")
print(s)
print(s1)
print(s2)
#Formatting Strings
# 1. Using f-strings: f-strings allows to directly insert variables and expressions inside a string using {} brackets.
# 2. Using format(): format() method allows inserting values into placeholders {} inside a string.
name = "Mani"
age = 20
print(f"Name: {name}, Age: {age}")
s="My name is {} and I am {} years old.".format(name,age)
print(s)
# String Membership Testing
print("My" in s)
print("You" in s)
#String Comparisions
s1 = "apple"
s2 = "banana"
print(s1 == s2)
print(s1 != s2)
print(s1 < s2)
print(s1 <= s2)
print(s1 > s2)
print(s1 >= s2)
#Convert integer to string in Python
n = 42
s = str(n)
print(s)
s = f"{n}"
print(s)
s = "{}".format(n)
print(s)
s = "%s" % n
print(s)
s = repr(n)
print(s)
#Lists
l=[10,20,30,40,50]
print(l)
l1=l[0]
print(l1)
del l[0]
print(l)
print()
l[1]=69
print(l)
print(l)
