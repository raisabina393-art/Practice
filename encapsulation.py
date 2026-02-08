#accessing private attribute
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.__salary=salary

    def show_salary(self):
        print(self.__salary)

e=Employee("ram", 10000)
print(e.name)
e.show_salary()

#accessing protected attributes.Single _ 
