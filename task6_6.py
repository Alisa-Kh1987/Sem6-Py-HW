# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# Было

# from math import pi
# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# 2й вариант (со словарем)

# from math import pi
# dict_pi = {}
# d = 1
# for d in range(1,11):
#     value = round(pi,d)
#     dict_pi[d] = value 
# print(dict_pi)

# # Стало
from math import pi
print(dict((enumerate((round(pi,d) for d in range (1,11)), start=1))))