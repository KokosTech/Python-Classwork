import random
import string
import tkinter as tk

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

# Testing - WM

def buton_click():
    com.add_employee(get_name.get(), get_email.get())
    for i in com.employees:
        label = tk.Label(text=f"{i.name} {i.email}")
    label.pack()


window = tk.Tk()
window.geometry("500x300")
window.title(com.name)

label = tk.Label(text="Welcome to the company")
label.pack()
label = tk.Label(text=com.name)
label.pack()

get_name = tk.Entry()
get_email = tk.Entry()
button = tk.Button(text='Add employee', command=lambda: buton_click())

get_name.pack()
get_email.pack()
button.pack()

for i in com.employees:
    label = tk.Label(text=f"{i.name} {i.email}")
    label.pack()

entry = tk.Entry()
submit_button = tk.Button()
window.mainloop()