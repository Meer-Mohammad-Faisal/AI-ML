#9. Write a program to find out whether a file is identical & matches the content of
#another file.

with open("chapter9_ps/log.txt") as f:
    content1 = f.read()

with open("chapter9_ps/file.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")

else:
    print("No these files are not identical")