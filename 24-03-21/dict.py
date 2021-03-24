import json
FILE_NAME = "students.json"

class Students:
    def __init__(self):
        self.students = {}

    def create_student(self, name, grades):
        self.students[name] = grades
        self.write_json()

    def write_file(self):
        with open(FILE_NAME, 'w') as f:
            json.dump(self.students, f, indent=4)
    
    def read_students(self):
        with open(FILE_NAME, 'w') as f:
            self.students = json.loads(f)

