#1. Write a program to read the text from a given file ‘poems.txt’ and find out
#whether it contains the word ‘twinkle’
f = open("chapter9_ps/poem.txt")
c = f.read()
if("twinkle" in c):
    print("twinkle is present in the content")
else:
    print("not present")