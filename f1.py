# # f=open("notes.txt","r")
# # print(f.read())
# # f.close() 
 
# # f=open("demo.txt","a")
# # f.write("hello demo")
# # f.close()

# f=open("demo.txt","w")
# f.write("hello demo on the data\n")
# f.close()
# data=["1\n","2,3,4,5,6\n"]
# with open("demo.txt","a") as f:
#     f.write("hello\n")
#     f.write("Python\n")
#     f.write("Java\n")
#     f.write("AI\n")
#     f.writelines(data)
name = input("Enter your name: ")

with open("students.txt", "a") as f:
    f.write(name + "\n")

numbers = [10, 20, 30]

with open("numbers.txt", "a") as f:
    for n in numbers:
        f.write(str(n) + "\n")    