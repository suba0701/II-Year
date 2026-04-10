from collections import namedtuple

Employee = namedtuple("Employee", ["name", "salary"])

employees = [
    Employee("Alice", 85000),
    Employee("Bob", 78000),
    Employee("Charlie", 92000),
    Employee("Diana", 88000),
]

# find employee with highest salary
highest = max(employees, key=lambda e: e.salary)
print(highest)           # Employee(name='Charlie', salary=92000)
print(highest.name)      # Charlie
print(highest.salary)    # 92000
