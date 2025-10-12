#4. Write a program to filter a list of numbers which are divisible by 5

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,445,7,78,95,5500,34545,78]
f =list(filter(divisible5,a))
print(f)