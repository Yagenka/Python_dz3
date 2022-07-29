
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def get_float (my_list: list):
   for i in range(len(my_list)):
       my_list[i] = round(my_list[i] % 1, 3)
   return (my_list)

def delete_0 (my_list: list):
   i = 0
   while i < len(my_list):
       if my_list[i] == 0:
          my_list.pop(i)
       else:
           i += 1
   return (my_list)

def max_min (my_list: list):
   max = my_list[0]
   min = my_list[0]
   for i in range(len(my_list)):
       if my_list[i] > max:
          max = my_list[i]
   for i in range(len(my_list)):
       if my_list[i] < min:
          min = my_list[i] 
   result = max - min
   return result

my_list = [1.1, 1545.2, 1513.33, 51515, 104.01]
float_list = get_float(my_list)
without_nule_list = delete_0 (float_list)
result = max_min (without_nule_list)
print(f'Разница между max и min значением дробной части элементов {result}')
