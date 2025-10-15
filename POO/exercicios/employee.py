from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_bonus(self) -> float:
        raise NotImplementedError


class Manager(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.4


class Developer(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.2


class Analyst(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.3


def main():
    employees: list[Employee] = [
        Manager("Alice", 10000),
        Developer("Bob", 8000),
        Analyst("Charlie", 9000),
    ]

    for employee in employees:
        print(f"{employee.name}'s bonus: ${employee.calculate_bonus():.2f}")


if __name__ == "__main__":
    main()
