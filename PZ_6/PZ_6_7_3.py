# Дан список размера N. Возвести в квадрат все его локальные минимумы (то есть числа, меньшие своих соседей).
import random
N = int(input("Размер списка: "))
a = []
for o in range(N):
    number = random.randint(1, 33)
    a.append(number)
print("Список",a)
for i in range(1, N - 1):
  if a[i] < a[i - 1] and a[i] < a[i + 1]:
    print("Найден минимум:", a[i])
    a[i] = a[i] ** 2
print("Результат: ", a)
