import random

n = random.randint(3, 20)


def porol():
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                print(f'  > ', i, ' - ', j)


def answer():
    print()
    print(*stone_1)
    for i in stone_2:
        print('  ', *i)


stone_1 = [n]
stone_2 = [['  * ', ' * '], [' - ', ' ', ' - ']]
print('Начнём игру -_*')
print(' || || || || || ||')
print(' _________________')
answer()
porol()
for i in stone_2:
    print('  ', *i)
print('Ты свободен! Забирай сокровище и Беги-и-и-и!')
