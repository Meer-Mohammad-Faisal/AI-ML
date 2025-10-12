#BASE CLASS
class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class Programeer:
#     company = "ITC INFOTECH"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
       

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

#INHERITED CLASS
class Programeer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programeer()

print(a.company,b.company)