
print ("Добро пожаловать в игру Крестики-Нолики!!")
M = [['-' for j in range(4)] for i in range(4)]

for i in range(4):
    M[0][i]=str(i-1)
for i in range(4):
    M[i][0]=str(i-1)
M[0][0]=''
print('\n'.join('\t'.join(map(str, row)) for row in M))


l = input('Введите координаты куда поставить "X"')

def hod (pole,tip,x,y):
    pole[x][y]=tip


hod (M,'x',1,2)

print('\n'.join('\t'.join(map(str, row)) for row in M))

# print('\n'.join('\t'.join(map(str, row)) for row in M))