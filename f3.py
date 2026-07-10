search="Configure"
start=False 
with open("Notes.txt","r") as f:
    for line in f:
        if search in line:
            start=True 
        if start:
            print(line,end=" ")    