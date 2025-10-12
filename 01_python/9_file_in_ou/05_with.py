f = open("chapter9/newfile.txt")
print(f.read())
f.close()

# the same can be written using with
# statment like this:
with open("chapter9/newfile.txt") as f:
    print(f.read())

#you dont have to explicitly close the file