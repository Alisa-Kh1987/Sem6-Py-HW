# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#Было:

# mult_N=1
# list = []
# N=int(input('Введите N: '))
# for i in range(1,N+1):
#     mult_N*=i
#     list.append(mult_N)

# print(list)

# Стало

from random import randint
my_list = [randint(-10, 10) for i in range(10)]
print(my_list)