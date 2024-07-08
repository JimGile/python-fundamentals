from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, fname: str, lname: str) -> None:
        self.fname: str = fname
        self.lname: str = lname

    @abstractmethod
    def calculate_paycheck(self):
        """Calculate the employee's weekly salary."""
        pass


class SalaryEmployee(Employee):
    def __init__(self, fname: str, lname: str, salary: float) -> None:
        super().__init__(fname, lname)
        self.salary: float = salary

    def calculate_paycheck(self) -> float:
        return self.salary/52


class HourlyEmployee(Employee):
    def __init__(self, fname: str, lname: str, weekly_hours: int, hourly_rate: float) -> None:
        super().__init__(fname, lname)
        self.weekly_hours: int = weekly_hours
        self.hourly_rate: float = hourly_rate

    def calculate_paycheck(self) -> float:
        return self.weekly_hours * self.hourly_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname: str, lname: str, salary: float, sales_num: int, comm_rate: float) -> None:
        super().__init__(fname, lname, salary)
        self.sales_num: int = sales_num
        self.comm_rate: float = comm_rate

    def calculate_paycheck(self) -> float:
        reg_sal = super().calculate_paycheck()
        comm = self.sales_num * self.comm_rate
        return reg_sal + comm
