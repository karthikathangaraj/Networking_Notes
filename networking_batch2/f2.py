with open("notes.txt", "r") as f:
    print(f.tell())

    data = f.read(5)
    print(data)

    print(f.tell()) 

with open("notes.txt", "r") as f:
    f.seek(200)
    print(f.read())    