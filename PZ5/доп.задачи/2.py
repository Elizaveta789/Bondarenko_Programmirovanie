a = int(input())

def all_summ(a):
    count = 0
    digit_sum = 0
    while a != 0:
        count += 1
        digit_sum += a % 10
        a //= 10
        if digit_sum == 0:
            break
    return count
print(all_summ(a))