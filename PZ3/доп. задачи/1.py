#Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном случае увеличить его в 1.5 раза
a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
n = a * b
if n < 0:
    n = n * 8
else:
    n = n * 1.5
print(n)