# Задайте число.
# Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonachi(n):
    if n in [1, 2]:
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)
 
def negafibonachi(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
    return negafibonachi(n + 2) - negafibonachi(n + 1)
 
n = int(input("Введите число - "))
my_list = []
for e in range(-n, -1):
    my_list.append(negafibonachi(e))
my_list.append(0)
for e in range(1, n + 1):
    my_list.append(fibonachi(e))
print('Список чисел Фибоначчи, включая отрицательные индексы:')
print(my_list)


