
# def power(A, B):
#     if B == 0:
#         return 1
#     elif B == 1:
#         return A
#     else:
#         return A * power(A, B-1)

# A = 3
# B = 5
# result = power(A, B)
# print(result) # Output: 243

# A = 2
# B = 3
# result = power(A, B)
# print(result) # Output 8


########################


# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return sum(a ^ b, (a & b) << 1)

# a = 2
# b = 2
# result = sum(a, b)
# print(result) # Output: 4

########################

# import re

# poem = input()  # Ввод стихотворения
# words = poem.split()  # Разбиваем стихотворение на список слов

# vowels = ['a', 'e', 'i', 'o', 'u', 'y']  # Список гласных букв (включая "y")
# vowel_count = 0  # Количество гласных в предыдущей фразе

# for word in words:
#     # Ищем гласные буквы в слове и считаем их количество
#     current_vowel_count = len(re.findall('[' + ''.join(vowels) + ']', word))

#     if vowel_count == 0:
#         vowel_count = current_vowel_count  # Если это первая фраза, запоминаем количество гласных
#     elif current_vowel_count != vowel_count:
#         print('Пам парам')  # Если количество гласных отличается от предыдущей фразы, ритма нет
#         break
# else:
#     print('Парам пам-пам') 


###############################


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         row = ""
#         for j in range(1, num_columns + 1):
#             row += str(operation(i, j)) + " "
#         print(row.strip())

# print_operation_table(lambda x, y: x * y)







