#1. Create a class “Programmer” for storing information of few programmers
#working at Microsoft.
class programmers():
    company = "Microsoft"
    def __init__(self, name, salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmers("Faisal", 200000,240000)
print(p.name, p.salary, p.pin, p.company)
r = programmers("Badal",299999,43566)
print(r.name, r.salary, r.pin,r.company)
