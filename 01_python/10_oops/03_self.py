class Employee:
    language = "python" #this is a class attribute
    salary = 200000
    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")


#self ko hmesha pass krna prega as a argument
# agar self se bachna hai to hme static method ka use krna prega 
#example:-

#statci mehthod
    @staticmethod
    def greet():
        print("Good morning")




harry = Employee()

harry.getInfo()



harry.greet()