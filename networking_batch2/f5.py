# import difflib 
# with open("file1.txt") as f1, open("file2.txt") as f2:
#     diff =difflib.unified_diff(
#         f1.readlines(),
#         f2.readlines(),
#         fromfile="file1",
#         tofile="file2"
#     )

# print("".join(diff))    


from itertools import zip_longest

with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip_longest(f1, f2, fillvalue=""):
       if l1 != l2:
            print("File1:", l1.strip())
            print("File2:", l2.strip())

