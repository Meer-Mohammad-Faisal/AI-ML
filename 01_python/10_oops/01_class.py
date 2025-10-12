class Employee:
    
    language = "py" # this is a class attrubute
    salary = 200000

badal = Employee()
badal.name = "faisal"# this is an instance or object attribute
print(badal.name,badal.language,badal.salary )

rohan = Employee()
rohan.name = "Rohan roro"
print(rohan.name,rohan.salary,rohan.language)


#here name is object attribute and salaray and language are calss 
#attribute as they directly belog to the class
