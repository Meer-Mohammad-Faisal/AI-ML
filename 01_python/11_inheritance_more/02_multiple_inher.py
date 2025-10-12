#PARENT CALSS 1
class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")


#PARETN CLASS 2
class Coder:
    language = "python"
    def printlangages(self):
        print(f"out of all the language here is your language: {self.language}")



#INHERITED CLASS
class Programeer(Employee,Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programeer()

b.show()
b.printlangages()
b.showLanguage()