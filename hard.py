import random

n = random.randint(3, 20)

def porol():
    if stone_1[n] == 3 and stone_2[[1],[2]]:
        result = 'Ты свободен'
    if stone_1[n] == 4 and stone_2[[1],[3]]:
        result = 'Ты свободен'
    if stone_1[n] == 5 and (stone_2[[1],[4]] or stone_2[[2],[3]]):
        result = 'Ты свободен'
    if stone_1[n] == 6 and (stone_2[[1], [2]] or stone_2[[1], [5]] or stone_2[[2], [4]]):
        result = 'Ты свободен'
    if stone_1[n] == 7 and (stone_2[[1], [6]] or stone_2[[2], [5]] or stone_2[[3], [4]]):
        result = 'Ты свободен'
    if stone_1[n] == 8 and (stone_2[[1], [3]] or stone_2[[1], [7]] or stone_2[[6], [4]] or stone_2[[3], [5]]):
        result = 'Ты свободен'
    if stone_1[n] == 9 and (stone_2[[1], [2]] or stone_2[[1], [8]] or stone_2[[2], [7]] or stone_2[[3], [6]] or stone_2[[4], [5]]):
        result = 'Ты свободен'
    if stone_1[n] == 10 and (stone_2[[1], [4]] or stone_2[[1], [9]] or stone_2[[2], [3]] or stone_2[[2], [8]] or stone_2[[3], [7]] or stone_2[[4], [6]]):
        result = 'Ты свободен'
    if stone_1[n] == 11 and (stone_2[[1], [10]] or stone_2[[2], [9]] or stone_2[[3], [8]] or stone_2[[4], [7]] or stone_2[[5], [6]]):
        result = 'Ты свободен'
    if stone_1[n] == 12 and (stone_2[[1], [2]] or stone_2[[1], [3]] or stone_2[[1], [5]] or stone_2[[1], [11]] or stone_2[[2], [4]] or stone_2[[2], [10]] or stone_2[[3], [9]] or stone_2[[4], [8]] or stone_2[[5], [7]]):
        result = 'Ты свободен'
    if stone_1[n] == 13 and (stone_2[[1], [12]] or stone_2[[2], [11]] or stone_2[[3], [10]] or stone_2[[4], [9]] or stone_2[[5], [8]] or stone_2[[6], [7]]):
        result = 'Ты свободен'
    if stone_1[n] == 14 and (stone_2[[1], [6]] or stone_2[[11], [3]] or stone_2[[2], [5]] or stone_2[[2], [12]] or stone_2[[3], [4]] or stone_2[[3], [11]] or stone_2[[4], [10]] or stone_2[[5], [9]] or stone_2[[6], [8]]):
        result = 'Ты свободен'
    if stone_1[n] == 15 and (stone_2[[1], [2]] or stone_2[[1], [4]] or stone_2[[11], [4]] or stone_2[[2], [3]] or stone_2[[2], [13]] or stone_2[[3], [12]] or stone_2[[4], [11]] or stone_2[[5], [10]] or stone_2[[6], [9]] or stone_2[[7], [8]]):
        result = 'Ты свободен'
    if stone_1[n] == 16 and (stone_2[[1], [3]] or stone_2[[1], [7]] or stone_2[[11], [5]] or stone_2[[2], [6]] or stone_2[[2], [14]] or stone_2[[5], [3]] or stone_2[[3], [13]] or stone_2[[4], [12]] or stone_2[[5], [11]] or stone_2[[6], [10]] or stone_2[[7], [9]]):
        result = 'Ты свободен'
    if stone_1[n] == 17 and (stone_2[[11], [6]] or stone_2[[2], [15]] or stone_2[[3], [14]] or stone_2[[4], [13]] or stone_2[[5], [12]] or stone_2[[6], [11]] or stone_2[[7], [10]] or stone_2[[8], [9]]):
        result = 'Ты свободен'
    if stone_1[n] == 18 and (stone_2[[1], [2]] or stone_2[[1], [5]] or stone_2[[1], [8]] or stone_2[[1], [17]] or stone_2[[2], [4]] or stone_2[[2], [7]] or stone_2[[2], [16]] or stone_2[[3], [6]] or stone_2[[3], [15]] or stone_2[[4], [5]] or stone_2[[4], [14]] or stone_2[[5], [13]] or stone_2[[6], [12]] or stone_2[[7], [11]] or stone_2[[8], [10]]):
        result = 'Ты свободен'
    if stone_1[n] == 19 and (stone_2[[1], [18]] or stone_2[[2], [17]] or stone_2[[3], [16]] or stone_2[[4], [15]] or stone_2[[5], [14]] or stone_2[[6], [13]] or stone_2[[7], [12]] or stone_2[[8], [11]] or stone_2[[9], [10]]):
        result = 'Ты свободен'
    if stone_1[n] == 20 and (stone_2[[1], [3]] or stone_2[[1], [4]] or stone_2[[1], [9]] or stone_2[[1], [19]] or stone_2[[2], [3]] or stone_2[[2], [8]] or stone_2[[2], [18]] or stone_2[[3], [7]] or stone_2[[3], [17]] or stone_2[[4], [6]] or stone_2[[4], [16]] or stone_2[[5], [15]] or stone_2[[6], [14]] or stone_2[[7], [13]] or stone_2[[8], [12]] or stone_2[[9], [11]]):
        result = 'Ты свободен'






def answer():
    print()
    print(*stone_1)
    for i in stone_2:
        print('  ', *i)

stone_1 = [n]
stone_2 = [['-', '-'], ['-', '-']]
print('Начнём игру -_*')
print(' || || || || || ||')
print(' _________________')
answer()
for popitka in range(1, 4):
    print(f'попытка: {popitka}')
    if popitka < 4:
        print()
        print('...       ТВОЙ ОТВЕТ     ...')
        print()
        nambe1 = int(input(' твоё первое число '))
        nambe2 = int(input(' твоё второе число '))
        stone_2[0][0] = nambe1
        stone_2[0][1] = nambe2
        answer()
        if porol() == 'Ты свободен':
            print('Ты свободен')
            break
    else:
        popitka = 4
        break
print('ВЫ НЕ МОЖЕТЕ УЙТИ. ВСЁ КОНЧЕНО.')