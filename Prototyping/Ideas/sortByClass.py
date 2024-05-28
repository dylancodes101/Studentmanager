from tabulate import tabulate

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}: {self.age}"

# List of Person objects
people = [Person('Alice', 30), Person('Bob', 25), Person('Charlie', 35)]

# Sort by name using sorted() and a lambda function
sorted_people = sorted(people, key=lambda person: person.age, reverse = True)

# Prepare data for tabulate
table = [[person.name, person.age] for person in sorted_people]

# Define headers
headers = ["Name", "Age"]

# Print the table
print(tabulate(table, headers, tablefmt="pretty"))
