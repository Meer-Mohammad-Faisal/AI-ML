#Write a program using functions to find greatest of three numbers.
a =  2
b = 3
c = 7
def greatest(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b 
    elif(c>b and c>a):
        return c

print(greatest(a,b,c))