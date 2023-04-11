# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

number_factoril = int(input("Введите число факториала"))

factorial = 1
count = 1
while count <= number_factoril:
    factorial *= count
    count += 1

print(factorial)

# factorial = 1                     // альтернативное решение
# while number_factoril > 1:
#     factorial *= number_factoril
#     number_factoril -= 1

# print(factorial)