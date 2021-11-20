# Иморты
from variables import a,b,c 
# Функции 
def f(N):
    return N+2

# Переменные
N = int(input())
x = f(N)
a = f'{N} + 2 = {x}'

# Запись результата выполнения функции в файл под названием file.txt
f = open('file.txt', 'a')
f.write(a+'\n')
f.close()


choise = input('Y, N? ~$ ')

if choise == 'Y':
    print(b+c)
else:
    print("Fuck U JONHY!")
    

