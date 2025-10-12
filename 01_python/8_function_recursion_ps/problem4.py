# 5. Write a python function to print first n lines of the following pattern:
def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n 

print(sum(4))