# with open("file1.txt") as f, open("file2.txt") as f1:
#     if f1.read() == f.read():
#         print("same data")
#     else:
#         print("no")    

with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1,l2 in zip(f1,f2):
        if l1.strip() != l2.strip():
            print("Diff..")
            print("File1",l1.strip())
            print("File2",l2.strip())