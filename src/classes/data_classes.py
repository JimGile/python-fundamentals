from dataclasses import dataclass


@dataclass
class Project:
    """
    This class definition creates a Project class with attributes name, payment, and client.
    """
    name: str
    payment: float
    client: str


class Employee:
    def __init__(self, name: str, age: int, salary: float, project: Project):
        """
        Initializes a new instance of the Employee class.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            salary (float): The salary of the employee.
            project (Project): The project that the employee is assigned to.

        Returns:
            None
        """
        self.name: str = name
        self.age: int = age
        self.salary: float = salary
        self.project: Project = project


p = Project("Django app", 20000, "Globomantics")
e = Employee("Ji-Soo", 38, 1000, p)
print(e.project)
