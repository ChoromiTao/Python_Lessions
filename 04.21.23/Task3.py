# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.

number = int(input("Введите число: "))
my_str = "number"

def Reverse(text: str):
    if len(text) == 1:
        return text
    return text[-1] + Reverse(text[:-1])
# есть фича: вмест всех строчек: return ('1' if n ==1 else f'{text} -> {Reverse(text[:-1])}')

my_str = input('Введите строку: ')
print(Reverse(my_str))