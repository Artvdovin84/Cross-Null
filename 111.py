
print ("Добро пожаловать в игру Крестики-Нолики!!")
M = [['-' for j in range(4)] for i in range(4)]

for i in range(4):
    M[0][i]=str(i-1)
for i in range(4):
    M[i][0]=str(i-1)
M[0][0]=''
print('\n'.join('\t'.join(map(str, row)) for row in M))


#l = input('Введите координаты куда поставить "X" (пример 2 0)')

def hod (pole,tip,x,y):
    if pole[x][y] == '-':
        pole[x][y]=tip
        return False
    else:
        print ('Поле занято, попробуй еще раз')
        return True
for i in range(1,10):
    s = True
    if i % 2 == 0:
        while s:
            l = input('Введите координаты куда поставить "О" (пример 2 0)')
            x, y = int(l[0]) + 1, int(l[2]) + 1
            s = hod(M, 'O', x, y)
    else:
        while s:
            l = input('Введите координаты куда поставить "X" (пример 2 0)')
            x, y = int(l[0]) + 1, int(l[2]) + 1
            s = hod(M, 'X', x, y)
    print('\n'.join('\t'.join(map(str, row)) for row in M))





# print('\n'.join('\t'.join(map(str, row)) for row in M))