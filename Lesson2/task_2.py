"""
Задание 2
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и
 кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел
 со знаком?

Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
 Главное: дополнить числа до двух разрядов нулём!
"""

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list[1:2] = ['05']
my_list[8:9] = ['+05']
my_list.insert(1, '"')
my_list.insert(3, '"')
my_list.insert(5, '"')
my_list.insert(7, '"')
my_list.insert(12, '"')
my_list.insert(14, '"')
# message = ' '.join(my_list)
print(my_list)
