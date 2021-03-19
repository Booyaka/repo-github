"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков:
"""
from random import randrange


def get_jokes():
    """
    Функция генерирует случайные числа (не больше len(list))
    :return: Возвращает "шутку" из трех слов случайно выбранных из трех листов
    """
    r_nouns = randrange(len(nouns))
    r_adverbs = randrange(len(adverbs))
    r_adjectives = randrange(len(adjectives))
    n = f'{nouns[r_nouns]} {adverbs[r_adverbs]} {adjectives[r_adjectives]}'
    return n


nouns = ["автомобиль", "лес", "огонь", "город", "дом", "ступня"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "зимой", "летом"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes())
