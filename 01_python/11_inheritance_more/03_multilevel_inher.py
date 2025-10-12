class Employee:
    a = 1

class Programeer(Employee):
    b = 2

class Manager(Programeer):
    c = 3

o = Employee()
print(o.a) #prints the a attribute
#print(o.b) # show an error as there is no b attribute in Employee class


o = Programeer()
print(o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)