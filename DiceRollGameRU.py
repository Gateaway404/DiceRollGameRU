from random import randint  # Импорт библиотеки для генерации случайных целых чисел

print("Привет, хочешь бросить кости? Чем больше выпавшее число, тем круче ты становишься!")
answer = str(input())
if answer == "Да" or answer == "да":
    print(f'Тебе выпало число {(randint(1, 6))} и {randint(1, 6)}. Ты хочешь попытать удачу еще раз?')  # Показ 
    # выпавшего числа с вариантом повторного броска 
    answer2 = str(input())
    if answer2 == "Да" or answer2 == "да":
        print(f'На этот раз тебе выпало число {(randint(1, 6))} и {randint(1, 6)}.')  # Результат повторного броска
    if answer2 == "Нет" or answer2 == "нет":
        print("А зря, ведь ты мог бы стать круче)")  # Отказ от повторного броска
if answer == "Нет" or answer == "нет":
    print(
        "Правильно, ведь твоя крутизна не зависит от псведо-случайных чисел")  # Отказ от первого броска и окончание 
    # игры
