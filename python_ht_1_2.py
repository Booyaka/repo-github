'''
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!
'''

qube_list = [int(f**3) for f in range(1, 1000) if f % 2 != 0]
print(qube_list)
result = 0
for f in qube_list:
    remainder = f % 10
    whole = f // 10
    amount = remainder + whole
    if amount % 7 == 0:
        result += amount
print(result)

qube_list_plus17 = [f + 17 for f in qube_list]
print(qube_list_plus17)
result = 0
for f in qube_list_plus17:
    remainder = f % 10
    whole = f // 10
    amount = remainder + whole
    if amount % 7 == 0:
        result += f
print(result)

result = 0 # попробовал вариант без создания нового списка
for f in qube_list:
    new_f = int(f + 17)
    remainder = new_f % 10
    whole = new_f // 10
    amount = remainder + whole
    if amount % 7 == 0:
        result += amount
print(result)

# s = int(input("here: ")) # не стал удалять
# son = 0
# while s > 0:
#     son = son + s % 10
#     s = s // 10
#     r = son + s
#     print(r)
# print(son)

# num = int(input("enter: "))
# sum = 0
# while (qube_list[i] !=0):
#     sum = sum + num % 10
#     num = num // 10
# print("Sum: ", sum)
