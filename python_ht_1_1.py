"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

duration = int(input("How many seconds do you want to spend having fun? "))
SEC_IN_MIN = 60
SEC_IN_HOUR = 60 * SEC_IN_MIN
SEC_IN_DAY = 24 * SEC_IN_HOUR

result_sec = duration % SEC_IN_MIN
result_min = duration // SEC_IN_MIN
result_hour = duration // SEC_IN_HOUR
result_day = duration // SEC_IN_DAY

if duration < SEC_IN_MIN and duration > 0:
    print("That's:", result_sec, "sec")
    print("You're boring.")
elif duration >= SEC_IN_MIN and duration < SEC_IN_HOUR:
    print("That's:", result_min, "min", result_sec, "sec")
    print("Is it enough for you?")
elif duration >= SEC_IN_HOUR and duration < SEC_IN_DAY:
    if result_hour == 1:
        print("That's", result_hour, "hour", result_min - result_hour * SEC_IN_MIN, "min", result_sec, "sec")
        print("It's kind of cool!")
    else:
        print("That's", result_hour, "hours", result_min - result_hour * SEC_IN_MIN, "min", result_sec, "sec")
        print("It's kind of cool!")
elif duration >= SEC_IN_DAY:
    print("That's", result_day, "day", result_hour - result_day * 24, "hour", result_min - result_hour * SEC_IN_MIN,
          "min", result_sec, "sec")
    print("That's huge!")
else:
    print("WHaaaat?")  # Не успел внести сюда все варианты
