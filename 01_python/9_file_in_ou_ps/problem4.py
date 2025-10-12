#   3. Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.
word = "Donkey"

with open("chapter9_ps/file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word,"#####")


with open("chapter9_ps/file.txt","w") as f:
    f.write(contentNew)