#Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить функцией с параметрами. Значения n и m программа должна запрашивать.
def calculate_sum(n, m):
    if n > m:
        n, m = m, n
        
    total_sum = 0
    current = n
    while current <= m:
        total_sum += current
        current += 1
    return total_sum
while True:
    try:
        n = int(input("Введите начальное число: "))
        m = int(input("Введите конечное число: "))
        result = calculate_sum(n, m)
        print(f"Сумма чисел ряда от {min(n, m)} до {max(n, m)} равна: {result}")
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введите корректные целые числа.")
