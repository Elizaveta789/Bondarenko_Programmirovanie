a, b, c = int(input('Введите двухзначное число - ')), int(input('Введите двухзначное число - ')), int(input('Введите двухзначное число - '))
def sum_digits(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum

a_sum = sum_digits(a)
b_sum = sum_digits(b)
c_sum = sum_digits(c)
print(a_sum, b_sum, c_sum)
print(f'Максимальная сумма: {max(a_sum, b_sum, c_sum)}')