inum = input("Please type a number: ")
fnum = 0
pnum = 1

print(fnum)
for i in range(int(inum)):
    fnum += pnum
    pnum = fnum
    print(fnum)
    