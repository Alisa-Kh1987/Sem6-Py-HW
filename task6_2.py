# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


#Было
# from random import randint

# n = int(input('Укажите размер списка: '))
# min = int(input('Введите минимальное значение диапазона: '))
# max = int(input('Введите максимальное значение диапазона: '))
# result_list = []
# my_list = []

# for i in range(n):
#     my_list.append(randint(min, max))
# print(my_list)

# for i in range((len(my_list)+1)//2):
#     result_list.append(my_list[i]*my_list[len(my_list)-1-i])
# print(result_list)

#Стало

from random import randint
my_list = [randint(-10, 10) for i in range(10)]
print(my_list)
result_list = [my_list[i]*my_list[-i-1] for i in range((len(my_list)+1)//2)]
print(result_list)