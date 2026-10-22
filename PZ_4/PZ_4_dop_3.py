# Найти и вывести на экран квадраты и кубы чисел от 2-5
n = 2
square = 0
cube = 0
while n <= 5:
    square = n ** 2
    cube = n ** 3
    print("Квадрат:", square, "Куб:", cube)
    n += 1