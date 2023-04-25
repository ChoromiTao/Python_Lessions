# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.

number = int(input("Введите число: "))
my_str = "number"

def Reverse(number):
    if len(s) == 1:
        return s
    return s[-1] + Reverse(number-1)

my_str += Reverse(number)
print(my_str)