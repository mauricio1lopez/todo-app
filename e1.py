import glob

myfiles = glob.glob("*.txt")
print(myfiles)
for filepath in myfiles:
    print(filepath)
    with open(filepath, 'r') as file:
        print(file.read())