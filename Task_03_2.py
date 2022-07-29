# Напишите программу, которая найдёт
# произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def multi_paru (list1: list):
    list_new = []
    for i in range((len(list1) + 1)//2):
       list_new.append(list1[i] * list1[len(list1) -1 - i])
    return(list_new)

my_list1 = [2, 3, 4, 5, 6]
my_list2 = [2, 3, 5, 6]
list_new1 = multi_paru(my_list1)
list_new2 = multi_paru(my_list2)
print(f'произведением пар чисел списка {my_list1} является {list_new1}')
print(f'произведением пар чисел списка {my_list2} является {list_new2}')