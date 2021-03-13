"""
Задание 5. * Вызов с командной строки
Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
Вывод курсов сделать в том же порядке, что присланные аргументы
Например:

python task4.py USD EUR
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05
"""
import sys

from utils import get_currency_rate

for currency in sys.argv[1:]:
    if currency.isalpha():
        exchange_rates = get_currency_rate(currency)
        print(exchange_rates, 'руб')
