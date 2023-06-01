# class PhoneBook:

#     new*
#     def __init__(self, path: str = 'phones.txt'):
#         self.phone_book: list[dict[str, str]] = []
#         self.path = path
    
#     new*
#     def open (self):
#         with open(self.path, 'r', encoding='UTF-8') as file:
#             data = file.readlines()
#         for contact in data:
#             contact = contact.strip().split(':')
#             new = {'id': contact[0], 'name': contact[1], 'phone': }