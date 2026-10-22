even_n = 0
n = 0
while n < 4:
    a = int(input("Введите число: "))
    if a % 2 == 0:
        even_n += 1
    n += 1
print("Количество четных чисел: ", even_n)