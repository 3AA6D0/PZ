# Написать программу, подсчитывающую количество цифр числа, используя функцию.
def countNum(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    print(count)
n = int(input("Введите число"))
countNum(n)