# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

number_seeking = int(input("Введите определяемое число: "))

number1 = 0
number2 = 1

index_number = 2

while number2 < number_seeking:
    number1, number2 = number2, number1+number2
    index_number +=1
if number2 != number_seeking:
    print("Число не относится к ряду Фибоначчи")
else:
    print(index_number)