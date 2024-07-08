from employee_abstract_base_class import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee


class Company:
    def __init__(self, name) -> None:
        self.name = name
        self.employees: list[Employee] = []

    def add_employee(self, new_employee) -> None:
        self.employees.append(new_employee)

    def display_employees(self) -> None:
        print('Current Employees')
        for i in self.employees:
            print(i.fname, i.lname)
        print('------------------')

    def pay_employees(self) -> None:
        print('Pay Employees')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('------------------')


def main():
    my_company = Company('Acme')
    my_company.add_employee(SalaryEmployee('Sarah', 'Hess', 50000))
    my_company.add_employee(HourlyEmployee('Jane', 'Doe', 40, 25.49))
    my_company.add_employee(CommissionEmployee('John', 'Smith', 250000, 5, 200))

    my_company.display_employees()
    my_company.pay_employees()


main()
