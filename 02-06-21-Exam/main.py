""" 
1. Приема при инициализация път до файл
2. Има функция за четене на файла
3. Има фунцкия за разделяне на файла на n броя отделни файлове, където n e броят редове в файла
4. Има фунцкия за търсене на броят символи в файла (.!?,) 
"""

class Symbol:
    symbols = [".", "!", "?", ","]

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as f:
            self.lines = f.readlines()
    
    def split_file(self):
        nol = 0
        for line in self.lines:
            nol += 1
            with open(str(nol) + ".txt", 'w') as f:
                f.write(line)

    # Rollback to see previous version with indexing every symbol 

    def sym_num(self):
        self.nos = 0
        for sym in self.symbols:
            for line in self.lines:
                self.nos += line.count(sym)
        print(f"The symbols {self.symbols} are {self.nos}.")


 

file1 = Symbol("text.txt")
file1.read_file()
file1.split_file()
file1.sym_num()