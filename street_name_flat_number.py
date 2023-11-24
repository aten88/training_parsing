# Импортируйте модуль для работы с регулярными выражениями.
import re

addresses = [
    ('Он проживал в городе Иваново на улице Наумова. '
     'Номер дома 125 был зеркальной копией его номера квартиры 521'),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.'
]

for address in addresses:
    # Напишите регулярное выражение.
    pattern = r'город.? (\w+).+?улиц.? (\w+).+?дом.? (\d+).+?квартир.? (\d+)'

    # Примените метод регулярных выражений, который
    # найдёт шаблон pattern в строке address.
    address_match = re.search(pattern, address)

    # Распечатайте названия городов и улиц, номера домов и квартир
    # из обеих строк.
    print(
        address_match.group(1), address_match.group(2),
        address_match.group(3), address_match.group(4)
        )