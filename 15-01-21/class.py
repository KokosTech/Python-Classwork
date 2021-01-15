# Exercise 1

print("Exercise 1:\n")


class Triangle:
    a = 0
    b = 0
    c = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def p(self):
        print(f"The perimeter of the triangle is: {self.a + self.b + self.c}")


obj = Triangle(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: ")))
obj.p()

# Exercise 2

print("Exercise 2:\n")


import os

# Core Game Functions


class Table:
    table = []

    def __init__(self):
        i = 1
        for row in range(3):
            self.table.append([])
            for _ in range(3):
                self.table[row].append(i)
                i += 1

    def print_table(self):
        clear()
        print("-------------")
        print(f"| {self.table[0][0]} | {self.table[0][1]} | {self.table[0][2]} |")
        print("----+---+----")
        print(f"| {self.table[1][0]} | {self.table[1][1]} | {self.table[1][2]} |")
        print("----+---+----")
        print(f"| {self.table[2][0]} | {self.table[2][1]} | {self.table[2][2]} |")
        print("-------------\n")

    def get_turn(self, player_name, symbol):
        num = int(input(f"{player_name}, choose a number: "))
        for row in range(3):
            for col in range(3):
                if self.table[row][col] == num:
                    self.table[row][col] = symbol
                    return

    def win_check(self):
        if self.table[0][0] == self.table[0][1] == self.table[0][2] or \
                self.table[1][0] == self.table[1][1] == self.table[1][2] or \
                self.table[2][0] == self.table[2][1] == self.table[2][2] or \
                self.table[0][0] == self.table[1][0] == self.table[2][0] or \
                self.table[0][1] == self.table[1][1] == self.table[2][1] or \
                self.table[0][2] == self.table[1][2] == self.table[2][2] or \
                self.table[0][0] == self.table[1][1] == self.table[2][2] or \
                self.table[0][2] == self.table[1][1] == self.table[2][0]:
            return True
        return False


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main Game
count = 0
names = []

symbols = {
    1: "X",
    2: "O"
}


table = Table()

names.append(input("Enter player one's name: "))
names.append(input("Enter player two's name: "))

while True:
    player_number = count % 2

    table.print_table()
    table.get_turn(names[player_number], symbols[player_number+1])

    if table.win_check():
        clear()
        print(f"{names[player_number]} has won!")
        break
    if count == 8:
        clear()
        print("Tie...")
        break

    count += 1
