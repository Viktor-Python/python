"""
# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором
ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
"""


def thesaurus(*names):
    list_of_name = {}
    for name in names:
        first = name[0]
        list_of_name.setdefault(first, [])
        list_of_name[first].append(name)
    return list_of_name


d = thesaurus("Иван", "Мария", "Петр", "Илья", "Виктор", "Анатолий", "Татьяна", "Тимур", "Олеся", "Юрий", "Дмитрий")
for first_letter in sorted(d.keys()):
    print(f'{first_letter}: {d[first_letter]}')
