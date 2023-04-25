# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

from random import randint

def new_list(minn, maxx, length):
    a = [randint(minn, maxx) for i in range(length)]
    return a

def uniq_dictionary(list1):
    uniq_dict = {}
    for number in list1:
            uniq_dict[number] = uniq_dict.get(number, 0) +1
    print(uniq_dict)
    return uniq_dict

def unic_pairs(dict_n: dict, count = 0):
    for values in dict_n.values():
            count +=values//2
    return count

a = new_list(1, 10, 15)
print(a)
new_dict = uniq_dictionary(a)
b = unic_pairs(new_dict)
print(b)

# print(my_list := [randint(0,10) for _ in range(30)])
# print(sum([my_list.count(item)//2 for i in set(my_list)]))