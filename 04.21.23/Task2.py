# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

number = int(input("Введите число: "))
count = 0
for item in range(1,number+1):
    if number%item == 0:
        count +=1
if count == 2:
    print("Число является простым")
else:
    print("Число не является простым")

# k = 0             // решение Семёна
# for i in range(2, number // 2+1):
#     if number % i == 0:
#         k = k+1

# if k <= 0:
#     print("Число простое")
# else:
#     print("Число не является простым")

# def is_simple(num: int) -> bool:
#     if num in [1,2]:
#         return True
#     for i in range(3, num// 2+1, 2):
#         if num %i == 0:
#             return False
#     return True

# number = input("Введите число: ")
# print(f'Число {number}' + ('простое' if is_simple(number) else 'комплексное'))