"""
ЗАДАНИЕ 1

Человеко-ориентированное представление интервала времени
Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:

1) до минуты: <s> сек;
2) до часа: <m> мин <s> сек;
3) до суток: <h> час <m> мин <s> сек;
4) сутки или больше: <d> дн <h> час <m> мин <s> сек

Например, если пользователь введет 4567 секунд, вывести:
1 час 16 мин 7 сек
"""

seconds = int(input("Введите количество секунд"))
days = str(seconds // 86400)
hours = (seconds % 86400) // 3600
minutes = (seconds // 60) % 60
sec = seconds % 60
if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)
if sec < 10:
    sec = '0' + str(sec)
else:
    sec = str(sec)
hours = str(hours)
if seconds < 60:
    print(sec + ' сек.')
if seconds < 3600:
    print(minutes + ' мин, ' + sec + ' сек. ')
if seconds < 86400:
    print(hours + ' час, ' + minutes + ' мин, ' + sec + ' сек. ')
if seconds > 86400:
    print(days + ' дн, ' + hours + ' час, ' + minutes + ' мин, ' + sec + ' сек. ')
