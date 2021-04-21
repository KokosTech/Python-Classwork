import os
import random

try:
    os.mkdir("DIR_TREE")
except FileExistsError:
    pass

os.chdir("DIR_TREE")

x = int(input("Input X: "))

for i in range(x):
    try:
        os.mkdir("DIR" + str(i))
    except FileExistsError:
        pass
    os.chdir("DIR" + str(i))
    for i in range(random.randint(1,10)):
        with open(str(i), "w") as f:
            f.write(str(i))
    os.chdir("..")