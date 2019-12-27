// Из урока 1

def Searching(x, y):
    for el in open:
        if x == el[0] and y == el[1]:
            return True
    return False


def PrintField():
    for i in range(5):
        for j in range(5):
            if Searching(i, j):
                print(f' {field[i][j]} ', end='\t')
            else:
                print('[ ]', end='\t')
        print()


field = [[-1, 1, 0, 1, 1],
         [1, 2, 1, 2, -1],
         [1, 2, -1, 2, 1],
         [-1, 2, 2, 2, 1],
         [1, 1, 1, -1, 1]]
count_of_mines = 5
count = 0
open = []
print('Приветствую в игре сапер! Для хода введите координаты клетки через пробел\nНумерация '
      'столбцов идет с единицы до пяти')

running = True

while running and count != 25:
    print('Введи координату')
    x, y = map(int, input().split())
    while x < 0 or y < 0 or x > 5 or y > 5:
        print('Неверные координаты! Попробуйте еще раз')
        x, y = map(int, input().split())
    x, y = x - 1, y - 1
    if field[x][y] != -1:
        open.append([x, y])
        PrintField()
    else:
        count_of_mines -= 1
        running = False
    count += 1

if count_of_mines == 5:
    print('Ты победил!')
else:
    print('Проигрыш :(')
