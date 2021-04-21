# Functions

def ex_1():
    print("Exercise 1:\n")

    def prime(num):
        if num > 2:
            for n in range(2, num):
                if num % n == 0:
                    return False
            return True
        return False

    def next_prime(num):
        while True:
            if prime(num):
                return num
            num += 1

    number = int(input("To see the next prime number, enter a number: "))
    print(f"Next prime number is {next_prime(number)}")


def ex_2():
    print("\nExercise 2:\n")

    def disarium(num):
        dig = len(str(num))
        temp = num
        sum_d = 0
        while temp > 0:
            d = temp % 10
            sum_d += (d ** dig)
            temp = temp // 10
            dig = dig - 1
        if sum_d == num:
            return True
        return False

    number = int(input("To check if a number is Disarium, enter a number: "))

    print(f'{"The number is Disarium!" if disarium(number) else "The number is NOT Disarium"}')


# Run Functions

ex_1()
ex_2()
