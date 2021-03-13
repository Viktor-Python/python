"""
Задание 2. Курс Валюты
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
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


while True:
    currency = input('Введите буквенный код валюты: ')
    if currency is None:
        print(get_currency_rate(currency), 'руб')
    else:
        print(get_currency_rate(currency))
