"""
ЗАДАНИЕ 2

Сумма цифр числа
Спросить у пользователя число и вывести в ответ сумму цифр этого числа.
Программа должна спрашивать числа у пользователя до тех пор, пока он не введет "0".
"""
while True:
    numbers = sum(map(int, list(input("Введите число: "))))
    if numbers == 0:
        break
    print(numbers)