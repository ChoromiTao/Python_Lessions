# Задача №17. Решение в группах Дан список чисел. 
# Определите, сколько в нем встречается различных чисел. 
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
import random

minn, maxx, length = -5, 5, 10

list_number = [random.randint(minn, maxx) for i in range(length)]
print(list_number)

for j in range(minn, maxx):         # это сделано, потому что я думала, что нужно ещё сделать частотный словарь
    count = 0
    for item in list_number:
        if item == j:
            count +=1
    if count > 0:
        print(f"Число {j} встречается {count} раз,", end=", ")

list_number = set(list_number)
print(f"а всего количество различных, то есть уникальных числел = {len(list_number)}")