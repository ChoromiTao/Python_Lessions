# Задача №19. Решение в группах Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число. 
# Input:   [1, 2, 3, 4, 5] k = 3 Output:  [4, 5, 1, 2, 3]

list_numbers = [i for i in range(int(input("Введите длину задаваемого списка: ")))]
index = input("На сколько будем сдвигать полученный список вправо?: ")
print(list_numbers)
while index>0:
    list_numbers.insert(0, list_numbers[-1])
    list_numbers.


print(list_numbers)