def hod (pole,tip,x,y):
    if pole[y][x] == '-':
        pole[y][x]=tip
        return False
    else:
        print ('Поле занято, попробуй еще раз')
        return True


def vvod(name):
    err=0
    while True:
        if err==0:
            l = input(f'Введите координаты куда поставить "{name}" (пример 0,0) ')
        elif err==1:
            l = input('Вы ввели некорректные координаты, попробуйте еще раз (пример 0,0) ')
        if len(l)==3:
            if l[0].isdigit() and l[2].isdigit() :
                if int(l[0]) >=0 and int(l[0]) <=2 and int(l[2]) >=0 and int(l[2]) <=2:
                    return l
                else:
                    err = 1
            else:
                err = 1
        else :
            err = 1



def proverka(s):
    s = s*3
    win= []
    for x in range (1,4):
        st=''
        for y in range(1,4):
            st = st+M[x][y]
        win.append(st)
    for y in range (1,4):
        st=''
        for x in range(1,4):
            st = st+M[x][y]
        win.append(st)
    st=''
    for x in range(1, 4):
        st=st+M[x][x]
    win.append(st)
    win.append(M[1][3]+M[2][2]+M[3][1])
    if s in win:
        return  True
    else:
        return False

print ("Добро пожаловать в игру Крестики-Нолики!!")

while True:
    s= input('''
     Меню:
     1-Начать новыю игру
     2-Правила игры
     3-Выход     
    ''')
    if s == '1':
        M = [['-' for j in range(4)] for i in range(4)]

        for i in range(4):
            M[0][i]=str(i-1)
        for i in range(4):
            M[i][0]=str(i-1)
        M[0][0]=''
        print('\n'.join('\t'.join(map(str, row)) for row in M))
        for i in range(1, 10):
            st = True
            vr = 'O' if i % 2 == 0 else 'X'
            while st:
                l = vvod(vr)
                x, y = int(l[0]) + 1, int(l[2]) + 1
                st = hod(M, vr, x, y)
            print('\n'.join('\t'.join(map(str, row)) for row in M))
            if proverka(vr):
                print (f'Подеба!!! Выйграли {vr} ')
                break
            if i == 9:
                print ('Ничья!!1')





    elif s == '2':
        print ('''Правила игры:
        Кре́стики-но́лики -логическая игра между двумя противниками на квадратном поле 3 на 3 клетки или бо́льшего размера (вплоть до «бесконечного поля»).
        Один из игроков играет «крестиками», второй — «ноликами».
        Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики). 
        Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали, выигрывает. 
        Если игроки заполнили все 9 ячеек и оказалось, что ни в одной вертикали, горизонтали или большой диагонали нет трёх одинаковых знаков, партия считается закончившейся в ничью.
        Первый ход делает игрок, ставящий крестики. ''' )
    elif s == '3':
        break
    else:
        print ('Введите корректно пункт меню')















