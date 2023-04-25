# 39. Даны два списка чисел. Требуется вывести те элементы первого списка (в том порядке, в каком они идут в первом списке), 
# которых нет во втором списке

from random import randint

def prompt(msg):
    a = int(input(msg))
    return a

def new_list(minn, maxx, length):
    a = [randint(minn, maxx) for i in range(length)]
    return a

def uniq_list(list1, list2):
    uniq_list = list()
    for item in list1:
        if item not in list2:
            uniq_list.append(item)
    return uniq_list

first_list = new_list(1, 10, 10)
second_list = new_list(1, 5, 10)
print(first_list, second_list, uniq_list(first_list, second_list), sep="\n")

# print(new_list := [i for i in list_1 if i not in list_2])