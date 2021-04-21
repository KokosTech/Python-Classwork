import os

# Core Game Functions


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_table(table):
    clear()
    print("-------------")
    print(f"| {table[0][0]} | {table[0][1]} | {table[0][2]} |")
    print("----+---+----")
    print(f"| {table[1][0]} | {table[1][1]} | {table    [1][2]} |")
    print("----+---+----")
    print(f"| {table[2][0]} | {table[2][1]} | {table[2][2]} |")
    print("-------------\n")


def get_turn(table, player_name, symbol):
    num = int(input(f"{player_name}, choose a number: "))
    for row in range(3):
        for col in range(3):
            if table[row][col] == num:
                table[row][col] = symbol
                return


# Start Game Functions


def create_table():
    table = []
    i = 1
    for row in range(3):
        table.append([])
        for _ in range(3):
            table[row].append(i)
            i += 1
    return table


# End Game Functions


def win_check(table):
    if table[0][0] == table[0][1] == table[0][2] or \
            table[1][0] == table[1][1] == table[1][2] or \
            table[2][0] == table[2][1] == table[2][2] or \
            table[0][0] == table[1][0] == table[2][0] or \
            table[0][1] == table[1][1] == table[2][1] or \
            table[0][2] == table[1][2] == table[2][2] or \
            table[0][0] == table[1][1] == table[2][2] or \
            table[0][2] == table[1][1] == table[2][0]:
        return True
    return False


# Main Game
count = 0
names = []

symbols = {
    1: "X",
    2: "O"
}


table = create_table()

names.append(input("Enter player one's name: "))
names.append(input("Enter player two's name: "))

while True:
    player_number = count % 2

    print_table(table)
    get_turn(table, names[player_number], symbols[player_number+1])

    if win_check(table):
        clear()
        print(f"{names[player_number]} has won!")
        break
    if count == 8:
        clear()
        print("Tie...")
        break

    count += 1
