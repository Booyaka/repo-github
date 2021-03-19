"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
"""

def num_translate(alert):
    for rus, eng in dict_of_numbers.items():
        if alert == rus:
            return eng


dict_of_numbers = {
    'один': 'one',
    'два': 'two',
    'три': 'three',
    'четыре': 'four',
    'пять': 'five',
    'шесть': 'six',
    'семь': 'seven',
    'восемь': 'eight',
    'девять': 'nine',
    'десять': 'ten'
}

alert = input('Пожалуйста, введите число одт одного до десяти и я переведу его на английский: ')
alert = alert.lower()
print(num_translate(alert))
