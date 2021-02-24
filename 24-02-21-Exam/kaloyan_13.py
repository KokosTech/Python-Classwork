f = open("file.txt", 'w')

for _ in range(4):
    f.write("Hello, World!\n")

f.close()