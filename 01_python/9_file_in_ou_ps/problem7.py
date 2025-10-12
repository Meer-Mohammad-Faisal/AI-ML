# 7. Write a program to find out the line number where python is present from ques 6.


with open("chapter9_ps/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line NO: {lineno}")
        break
    lineno += 1

else:
    print("NO pytho is present")

