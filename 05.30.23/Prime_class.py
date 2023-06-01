class Car:
    class_atr = 0

    def __init__(self, label: str, color: str, year: int, audio: str = 'Нет'):
        self.label = label
        self.color = color
        self.year = year
        self.audio = audio

    def __str__(self):
        return f'Машина марки {self.label} {self.color} цвета {self.year} года выпуска'

    def drive(self):
        print('Брррррррр-р-р-р-р-р-р')

my_car = Car('Мазда', 'чёрный', 2019)
new_car = Car('Мерседес', 'бэлый', '2023')
old_car = Car('Жигули', 'коричневый', '1945')

my_car.audio = 'Долбит нормально'

print(my_car)
print(new_car)
print(old_car)

auto_park = [my_car, new_car, old_car]

# for car in auto_park:
#     print(car.audio)
