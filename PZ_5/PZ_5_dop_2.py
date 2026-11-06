# Расчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в функции.
def perimetr(a, b):
    return a*2 + b*2
def area(a, b):
    return a * b
a, b = int(input("Введите число")), int(input("Введите число"))
print("Периметр:", perimetr(a, b), "Площадь:", area(a, b), sep=' ')