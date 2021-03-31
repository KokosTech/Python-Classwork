import random
import string

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.id = self.id_generator()
    
    @staticmethod
    def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def print_employee(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Email: {self.email}")


class Company:
    def __init__(self, name):
        self.name = name;
        self.employees = []
    
    def print_employees(self):
        for i in self.employees:
            i.print_employee()
            print('\n')

    def add_employee(self, name, email):
        self.employees.append(Employee(name, email))


# Testing

com = Company("Hello There Corp.")
com.add_employee("Kirco Kirkov", "gdfgfd@hello.there")
com.add_employee("Kirco Mihaylov", "gg@hello.there")
com.print_employees()