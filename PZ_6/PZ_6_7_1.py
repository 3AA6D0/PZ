# Дан целочисленный список размера 10. Вывести все содержащиеся в данном списке нечетные числа в порядке возрастания их индексов, а также их количество K. 
import random
nums = []
for i in range(10):
    num = random.randint(1, 33)
    nums.append(num)
print("Список", nums)
n_num = []
k = 0
for x in nums:
    if x % 2 != 0:
        n_num.append(x)
        k += 1
n_num.sort()
print("Нечетные", n_num)
print("Количество K:",k)