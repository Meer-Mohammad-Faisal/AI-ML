class Employee:
    language = "python" #this is a class attribute
    salary = 200000

    def __init__(self,name,salary,language): # dunder method which is automaticallly called
        self.name = name
        self.salary = salary
        self.language = language
        print("I ama creating an object")


    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")

#self ko hmesha pass krna prega as a argument
# agar self se bachna hai to hme static method ka use krna prega 
#example:-
#statci mehthod
    @staticmethod
    def greet():
        print("Good morning")




harry = Employee("Harry", 130000, "javascript ")
#harry.name = "Harry"
print(harry.name, harry.salary,harry.language)



