#Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2
a, b = int(input('Введите число - ')), int(input('Введите число ещё раз - '))
d = a + b
if d % 5 == 0:
  d += 1
else:
  d -= 2
print(d)