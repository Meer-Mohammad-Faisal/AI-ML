# 11. Write a python program to rename a file to “renamed_by_ python.txt.
with open("chapter9_ps/old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt","w") as f:
    f.write(content)