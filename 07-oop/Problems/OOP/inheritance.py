# Implement the following classes to understand inheritance in Python:

# Class Name: Employee
# Attributes:
# id (int)
# salary (int)
# Constructor: __init__(self, id, salary) — Initializes the values to respective variables.

# Class Name: SalesEmployee (Subclass of Employee)
# Attributes:
# Inherited from Employee: id, salary
# New attribute: sales (int)
# Constructor: __init__(self, id, salary, sales) — Calls super().__init__(id, salary) to initialize id and salary, and initializes the sales attribute.

class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary
        
class SalesEmployee(Employee):
    def __init__(self, id, salary, sales):
        super().__init__(id, salary)
        self.sales = sales


id = int(input('Enter Employee ID:'))
salary = int(input('Enter Salary of the Employee:'))
sales = int(input('Enter no. of sales by the Employee:'))

Salesman = SalesEmployee(id, salary, sales)

print(Salesman.id)
print(Salesman.salary)
print(Salesman.sales)