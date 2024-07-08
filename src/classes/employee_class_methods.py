from datetime import date


class Employee:
    # Class level properties shared by all instances
    minimum_wage: float = 1000

    @classmethod
    def change_minimum_wage(cls, new_wage: float):
        if new_wage > 3000:
            raise ValueError("Company is bankrupt.")
        cls.minimum_wage = new_wage

    # Constructor
    @classmethod
    def new_employee(cls, name: str, dob: date):
        now: date = date.today()
        age: date = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    def __init__(self, name: str, age: int, salary: float):
        self.name: str = name
        self.age: int = age
        self.salary: float = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError('Minimum wage is ${Employee.minimum_wage}')
        self._salary = salary


print(Employee.minimum_wage)
Employee.change_minimum_wage(200)
print(Employee.minimum_wage)

e: Employee = Employee.new_employee("Mary", date(1991, 8, 12))
print(e.name)
print(e.age)
print(e.salary)
