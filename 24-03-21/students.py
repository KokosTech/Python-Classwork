import os
import json 

class Students:
    def __init__(self, name, file_name):
        self.file_name = file_name
        self.read_students(name)

    def create_student(self, name):
        self.read_students(name)

    def add_grade(self, name, grade):
        self.read_students(name, grade)

    # File Handling

    def write_json(self, data):
        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)

    # File Functions

    def read_students(self, name, grade = 0):
        if os.path.exists(self.file_name) and not os.stat(self.file_name).st_size == 0: # Правим тази двойна проверка, 
            with open(self.file_name, "r") as f:                                        # защото файлът може да е празен
                                                                                        # т.е. няма да има главната структура
                data = json.load(f)

                for student in data["Students"]:
                    if student["Names"] == name:
                        if grade > 0:
                            tempy = student["Grades"]
                            tempy.append(grade)

            temp = data["Students"]
            temp.append(
                {
                    "Names": name,
                    "Grades": tempy
                }
            )
            self.write_json(data)
            return []
        else:
            self.write_json(
                {
                    "Students": [{
                        "Names": name,
                        "Grades": []
                }]
                }
            )
            return []


# Testing

students = Students("Kristiyan Bogdanov", "stud.json")
students.add_grade("Kristiyan Bogdanov", 6)

