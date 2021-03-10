"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
"два"
"""
translate = {'zero': 'ноль',
             'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четыре',
             'five': 'пять',
             'six': 'шесть',
             'seven': 'семь',
             'eight': 'восемь',
             'nine': 'девять',
             'ten': 'десять'}


def num_translate(num):
    if not num.islower():
        return print(translate.get(num.lower()).title())
    else:
        return print(translate.get(num))


while True:
    num_translate(input('Введите числительные от 0 до 10: '))
