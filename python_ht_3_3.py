"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
"""

def thesaurus(name_list):
    my_list = {}
    index = 0
    for name in name_list:
        if name_list[index][0] not in my_list:
            my_list.setdefault(name_list[index][0], name)
        elif name_list[index][0] in my_list:
            list(my_list[name[0]]).append(name[1])  # Тут я поплыл и не могу понять какое условия записать
            print('Bug')
        index += 1
    return my_list


name_list = ['Jhonn', 'Alisha', 'Bob', 'Leonard', 'David', 'Jack']
print(thesaurus(name_list))
