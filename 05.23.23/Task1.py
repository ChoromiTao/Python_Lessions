# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# 1. Открыть файл +
# 2. Сохранить файл
# 3. Показать тк +
# 4. Добавить контакт +
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

path = 'phonebook.txt'

def create_open_file():
    data = open(path, 'a', encoding='UTF-8')
    data.close

def adding_into_file():
    data = open(path, 'a', encoding='UTF-8')
    name = input("Введите имя: ").capitalize()
    middle_name = input("Введите отчество: ").capitalize()
    surname = input("Введите фамилию: ").capitalize()
    phone = input("Введите номер телефона: ")
    data.write(f"{name} {middle_name} {surname} {phone}")
    data.close()

def reading_file():
    data = open(path, 'r', encoding='UTF-8')
    print(data.read())
    data.close()

def finding_contact_file():
    data = open(path, 'r', encoding='UTF-8')
    finding_contact = input("Введите искомый параметр: ")
    in_finding_text = data.readlines()
    # dict_contacts = {}
    # for i, j in enumerate(in_finding_text, 1):
    #     j = j.strip().split()
    #     dict_contacts = {'name': in_finding_text[0], 'middle_name': in_finding_text[1], 'surname': in_finding_text[2], 'phone': in_finding_text[3]}
    for i in in_finding_text:
        if i == finding_contact:
            print('yes')

finding_contact_file()