# def greet(name):
#     print("hello",name)

# name=input()
# greet("karthika")
# greet(name)    

# Function with Return Value 

# def add():
#     n1=int(input("enter the number "))
#     n2=int(input("enter the number"))
#     return n1+n2
# print("Result",add())
# sum=add()
# print("resu",sum**2)
# s1=add()
# print(s1)


# def sqr(l,b):

#     return l*b

# len=int(input())
# bre=int(input())
# ans=sqr(len,bre)
# print(ans)

# l1=[1,2,3,4,5]
# print(sum(l1))

#lambda

# sqr=lambda l,b:l*b
# print(sqr(1,3))


# even=lambda x: x%2 == 0
# leap=lambda year:(year %400 ==0 ) or (year % 4==0 and year %100 !=0) 
# print(leap(2004))
# print(even(92))

# max=lambda a,b,c: a if a>b and a >c else b if b>c else c  
# a,b,c=map(int,(input().split()))
# print(max(a,b,c))
def greet(name):      # name is a parameter
    print("Hello", name)
greet("Karthika")       

# 1. Positional Parameters
def add(a, b):
    print("Sum =", a + b)

add(10, 20)

# 2. Keyword Parameters (Keyword Arguments)

def student(age,name=None, ):
    print("Name:", name)
    print("Age:", age)

student(age=27,name="arthika")    

def add(*a):
    print(sum(a))
add(1,2)
add(1,2,3,4)
def details(**student):
    for key, value in student.items():
        print(key, ":", value)

details(name="Karthika", age=25, city="Chennai")   
details( age=25, city="Chennai")
