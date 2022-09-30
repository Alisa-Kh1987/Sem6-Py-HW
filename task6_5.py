# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Было
# from encodings import utf_8 
  
# with open("str_example.txt", encoding='utf_8') as fin: 
#     for line in fin: 
#         words = line.split() 
#         for word in words: 
#             if 'абв' in word: 
#                 words.remove(word) 
#         sentence = " ".join(words) 
#         print(sentence)

# Стало

# key = 'asd'
# my_list = list(map(str, input('Введите элементы списка: ').split()))
# new_list = list(filter(lambda i: key not in i , my_list))
# print(new_list)

# еще вариант
key = '777'
my_list = list(map(str, input('Введите элементы списка: ').split()))
res_list = [i for i in my_list if key not in i]
print(res_list)