def ex1():
    print("\nEx. 1:")

    string = input("Enter a string: ")
    out = str()

    for chr in string:
        if chr in "AEIOUaeiouАЪОУЕИаъоуеи":
            for i in range(4):
                out += chr
            continue;
        out += chr
    
    print(out)

def strlen(dgt):
    num = 0
    for i in dgt:
        num += 1
    return num

def ex2():
    dgt = input("Type a number: ")
    print(strlen(dgt))

def ex3():
    count = 0
    num = int(input("Type a number: "))

    import math

    while num >= 2:
        num = math.sqrt(num)
        count += 1

    print(count)

def is_prime(num):
    if num > 2:
        for i in range(2,num):
            if (num % i) == 0:
                return 0
            else:
                return int(num)
    elif num == 2:
        return 2
    else:
        return 0

def ex4():
    all = 0
    num = int(input("Type a number: "))

    for i in range(num + 1):
        all += is_prime(int(i))

    print(all)
    
ex4()