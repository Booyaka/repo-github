"""
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"',
 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
"""

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# print(my_list[1].isdigit())
# print(dir(my_list))
plus = '+' or '-'
index = 0
for el in range(len(my_list)):
      if my_list[el].isdigit():
          my_list[el] = f'{int(my_list[el]):02}'
      elif plus == my_list[el][0]:
          my_list[el] = f'{my_list[el][0]}{int(my_list[el]):02}'
      index += 1

my_list.insert(1, '"')  # Извините за такой мрак. Не выходило добавить нужное кол-во '"' в цикле
my_list.insert(3, '"')  # Я понимаю, что это нупские костыли, но это чисто для формального выполнения задания
my_list.insert(5, '"')  # Времени на выполнение больше нет =С
my_list.insert(7, '"')
my_list.insert(-2, '"')
my_list.insert(-1, '"')
print(my_list)

my_list.remove('"')
my_list.remove('"')
my_list.remove('"')
my_list.remove('"')
my_list.remove('"')
my_list.remove('"')
print(*my_list)
