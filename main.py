# coin_number, zero, one= int(input ("Введите число монет:")),0,0
# while zero+one<coin_number :
#     n = int(input("Произвольный набор 0/1 ->"))
#     if n == 0 : zero = zero + 1 
#     else : one = one +1
# print(f"Переверните {zero} монет/ы"if zero<one else f"Переверните {one} монет/ы")



# S = int(input("Введите сумму чисел: "))
# P = int(input("Введите произведение чисел: "))

# for i in range(1, P+1):  # перебираем все возможные делители числа P
#     if P % i == 0:
#         x = i
#         y = P // i
#         if x + y == S:  # если сумма равна S
#             print('X =', x, 'Y =', y)
#             break
# else:  # этот блок выполнится, если ни один делитель не подошел
#     print('Не могу найти числа X и Y')


n = int(input("Введите число N: "))
power_of_two = 1
while power_of_two <= n:
    print(power_of_two)
    power_of_two *= 2



    










