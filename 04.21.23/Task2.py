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