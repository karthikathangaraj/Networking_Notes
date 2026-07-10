# age=int(input("enter the age : "))
# if (age>=18) and (age<=110):
#     print("right to vote")
# else:
#     print("sorry n vote")    
# print("pro")    

# server_status = "UP"
# if server_status == "UP":
#     print("Server is reachable")

# port=int(input())
# if port == 22:
#     print("ssh port")
# elif port == 80:
#     print("HTTP port")   
# elif port == 443:
#     print("HTTPs port") 
# else:
#     print("unknown port")         

# if port == 80 or port == 443 or port == 22:
#     print("valid port")
# else:
#     print("sorry")   


user=input()
pass1=input()
if user == "admin":
    if pass1 == "123":
        print("login way")
    else:
        print("pass incorrect")
else:
    print("user incorrect...")            
bandwidth = 85

if bandwidth > 90:
    print("Critical Usage")
elif bandwidth > 70:
    print("High Usage")
else:
    print("Normal Usage")