# Brain game
# Guess the number

from random import randint


print('Угадайте число от 1 до 1000')
print('У вас 10 попыток')
number = randint(1, 1000)
for i in range(1, 11):
    print('Попытка', i)
    ask = int(input('Введите число: '))
    if ask < 1 or ask > 1000:
        print('GameError')
        print('Вводите числа от 1 до 1000')
        break
    elif ask == number:
        print('Угадали!')
        print(f'Именно число {number} я загадал')
        break
    elif ask < number:
        print('Введите число больше', ask)
    elif ask > number:
        print('Введите число меньше', ask)
else:
    print('Не угадали, попробуйте снова')
    print('Было загадано число', number)
