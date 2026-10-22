# Найти и вывести на экран S=1!+2!+3!+...+n!(n>1)
from math import factorial

n = int(input("Введите число: "))
k = 1
fact = 1
s = 0
while k <= n:
    fact *= k
    s += fact
    k += 1
print(s)