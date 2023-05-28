# Задача 18: Требуется найти в списке A самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
new_list = [randint(-10, 10) for i in range(int(input('Введите размер массива: ')))]
print(new_list)
x = int(input('Введите число: '))
element = new_list[0]
dif = abs(x - element) #встроенная функция, возвращающая абсолютное значение числа
count = 1

while count < len(new_list):
    dif_1 = abs(x - new_list[count])
    if dif_1 < dif:
        dif = dif_1
        element = new_list[count]
    count +=1

print('Самый близкий элемент к заданному числу: ',(element))    