#Составить функцию, которая напечатает сорок любых символов
import random
import string

def simbols_random():
    result = ''
    letters = string.ascii_letters
    digit = string.digits
    simvols = string.punctuation
    randomizer = letters + digit + simvols
    for i in range(40):
        random_char =  random.choice(randomizer)
        result += random_char
    return result
print(f'Сорок любых символов: {simbols_random()}')
