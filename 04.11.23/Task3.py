# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель 
# за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись 
# исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.
import random

month = 30
count = 0
max_count = 0
today = 0

for i in range(month):
    today += random.randint(-3,3)
    print(today, end=" ")
    if today > 0:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print(f"\nМаксимальное число тёплых дней: {max_count} дней (день/дня)")