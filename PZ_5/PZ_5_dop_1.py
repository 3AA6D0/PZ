# Даны три целых числа. Определить у какого числа больше сумма. Вывод результата предусмотреть в основой программе.
# Расчет суммы цифр оформить в функции.
def sum_num(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

a,b,c = int(input("Введите число")), int(input("Введите число")), int(input("Введите число"))
sum_a = sum_num(a)
sum_b = sum_num(b)
sum_c = sum_num(c)
if sum_a > sum_b and sum_a > sum_c:
    print("Наибольшая сумма у числа:", a,"Сумма цифр:", sum_a, sep = ' ')
elif sum_b > sum_c and sum_b > sum_a:
    print("Наибольшая сумма у числа:", b,"Сумма цифр:", sum_b, sep = ' ')
elif sum_c > sum_b and sum_c > sum_a:
    print("Наибольшая сумма у числа:", c,"Сумма цифр:", sum_c, sep = ' ')