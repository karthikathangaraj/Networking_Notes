# a=int(input())
# b=int(input()) 
# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)
# # print(a//b)
# # print(a**b) 
# # print(a != b)
# # print(a==b)
# # print(a>b)
# # print(a<b)
# # print(a>=b)
# # print(a<=b)
# print(a<b and a>b) #a=10 b=20 
# print(a<b or a<=b)
# print(not(a<b))

# a=10
# c=20
# a +=20 # a=a+20 c*=20 c=c*20
# print(a)

a=2     #0010
b=4     #0100 
#5 (5+1) -6 (-5) 4
#<<  a=5 b=2 a<<b
'''
5== 010100
>> 
5>>2 01
'''
print(a&b)
print(a|b)
print(a^b)
print(~(-5)) 
print(5<<2)
print(5>>2)

a=[1,2,3,4,5]
print(51 not in  a)

name="karthika"
name1="karthika"
print("A" in name)
print(name is not name1)
# from calculs import *
import calculs as c1
c1.add(1,2)
c1.sub(2,3)

from math import sqrt, factorial
print(sqrt(64))
print(factorial(4))