# a = {3, 5, 2, 7, 1}  
# a.update({1, 2, 3, 4, 5})  
# print(a)  


n = int(input("Введите число кустов на грядке: "))
a = [int(x) for x in input("Введите количество ягод на каждом кусте через пробел: ").split()]
max_berries = 0

for i in range(n):
    berries = a[i]
    if i > 0:
        berries += a[i-1]
    if i < n-1:
        berries += a[i+1]
    max_berries = max(max_berries, berries)

print("Максимальное число ягод, которые можно собрать за один заход собирающего модуля:", max_berries)


