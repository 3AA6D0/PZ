# Дан список размера N. Найти минимальный из его локальных максимумов (локальный минимум — это элемент, который меньше любого из своих соседей). 
import random
N = int(input("Размер списка: "))
a = []
for i in range(N):
  a.append(random.randint(1, 33))
print("Список", a)
local_max = []
for i in range(1, N - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        local_max.append(a[i])
if local_max:
    print("Локальные максимумы:", local_max)
    min = local_max[0]
    for x in local_max:
        if x < min:
            min = x
    print("Минимальный из них:", min)
else:
    print("Локальных максимумов нет")