#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Было: 

# N = int(input('Введите число N: '))
# my_list = []
# for i in range(1, N+1):
#     if(N%i==0):
#         my_list.append(i)
# print(my_list)

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")

# Стало

# from random import randint

n = int(input('Укажите n: '))
res_list = [i for i in range(1, n+1) if n%i == 0]
print(res_list)