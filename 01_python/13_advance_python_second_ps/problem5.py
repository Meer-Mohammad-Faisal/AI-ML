from functools import reduce
#5. Write a program to find the maximum of the numbers in a list using the reduce function.

l = [1,2,445,7,78,95,5500,34545,78]


def grater(a,b):
    if(a>b):
        return a 
    return b

print(reduce(grater,l))