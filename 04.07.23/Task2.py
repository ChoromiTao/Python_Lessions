# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.

a = int(input("Введите количество учеников 1 класса: "))
b = int(input("Введите количество учеников 2 класса: "))
c = int(input("Введите количество учеников 3 класса: "))

print(f"Ответ: {int(((a + 1) // 2) + ((b + 1) // 2) + ((c + 1) // 2))}")