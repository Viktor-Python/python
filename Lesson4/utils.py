"""
Задание 4. Модуль utils
Написать свой модуль utils и перенести в него функцию get_currency_rate() из предыдущего задания (второго или третьего).
Создать скрипт (task4.py), в котором импортировать этот модуль и выполнить вызовы
функции get_currency_rate() для доллара и евро. Результат вывести на экран в виде:

если используется функция из 2-го задания:
USD 75.18
EUR 80.35
либо, если используется функция из 3-го задания
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05
"""
import requests


def get_currency_rate(currencies):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if resp.status_code != 200:  # Ok
        print('Данные с сайта ЦБ РФ не доступны')
        exit()
    content = resp.content.decode('windows-1251')

    parts = content.split('</Valute><Valute')
    currency_code = '<CharCode>' + currencies.upper() + '</CharCode>'
    for part in parts:
        if currency_code in part:
            break
    else:
        return None

    currency_rate = float(part.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))
    currency_denomination = (part.split('<Name>')[1].split('</Name>')[0])
    date = (content.split('<ValCurs Date=')[1].split(' name="')[0])
    result = date + ' ' + currency_denomination + ' - ' + str("{0:.2f}".format(currency_rate))

    return result


