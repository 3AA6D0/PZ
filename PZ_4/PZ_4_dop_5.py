# Ввести N чисел. Найти и вывести их среднее арифметическое
n = int(input("Введите число:"))
k = 0
arithmetic_num = 0
sum = 0
while k < n:
    a = int(input(f"Введите число {k+1}: "))
    sum += a
    k += 1
arithmetic_num = sum / 2
print(arithmetic_num)