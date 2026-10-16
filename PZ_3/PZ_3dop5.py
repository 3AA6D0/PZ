# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
result = num1 + num2
if result % 5 == 0:
  print(result + 1)
else:
  print(result - 2)
