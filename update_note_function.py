# Этап3_Финальное_Юнин_Константин.
# Задание 2: Функция обновления заметки
import re
from datetime import date, datetime

note_states = {'username': 'Алексей',
               'title': 'Список покупок',
               'content': 'Купить продукты на неделю',
               'status': 'новая',
               'created_date': '10.01.2025',
               'issue_date': '17.01.2025'}    # Список словарей заметки
note = ['username', 'title', 'content',
        'status', 'created_date', 'issue_date']
status_ = ("новая", "в процессе", "выполнено")  # Список статусов заметки для ввода
fraza = {0: "Вы ввели текст без заглавной буквы, поэтому повторите ввод!",
         1: "Вы ввели заголовок, который уже вводили ранее, поэтому повторите ввод заголовка заметки!",
         2: "Вы ввели несколько заголовков, поэтому повторите ввод заголовка заметки!",
         3: "Вы неправильно ввели статус заметки,(новая, в процессе, выполнено), поэтому повторите ввод!",
         4: "Неверный формат даты. Пожалуйста, убедитесь, что дата введена правильно.",
         5: "Дата дедлайна не может быть раньше даты создания заметки, повторите ввод!"}                                   # Словарь фраз для вывода


def update_note():
    global vvod_, pole
    print("Текущие данные заметки: ")
    print(note_states)
    while True:
        vvod_ = input("Какие данные вы хотите обновить? (username, title, content, status, issue_date): ")
        if vvod_ in note:
            while True:
                pole = input("Введите новое значение для " + vvod_ + " : ")
                pro_ = proverka(
                    pole, note.index(vvod_)
                                )               # Проверка вводимых данных
                if pro_ == 0:
                    continue                    # Выход из цикла для повторного ввода
                else:
                    if (input(
                            "Вы уверены, что хотите обновить поле? (да/нет) "
                              ) in [
                        "да", "Да", "Y", "y", "Yes", "yes"
                                        ]):     # Проверка на необходимость изменения словаря
                        note_states[vvod_] = pro_   # Изменение словаря заметки по ключу
                        print("Заметка обновлена: ")
                        print(note_states)
                    else:
                        print("Заметка не обновлена!")
                    if (input(
                            "Вы хотите продолжить? (да/нет) "
                              ) in [
                        "да", "Да", "Y", "y", "Yes", "yes"
                                    ]):         # Проверка на необходимость изменения словаря
                        break
                    return
        else:
            print("Вы ввели некорректное значение, пожалуйста повторите ввод!")
            continue

def proverka(stroka_, ind_):                    # Проверка вводимых данных
    counter = 0                                 # Счетчик заглавных букв
    if ind_ in [4, 5]:
        stroka_ = replace_dates(stroka_)        # Проверка на ввод даты и преобразование в тип datetime
        if stroka_ == 0:
            return 0                            # Данные не прошли проверку. Выход из функции с аргументом 0
        if ind_ in [5] and (
                stroka_ - date.today()
                            ).days <= 0:        # Дата создания меньше или равна даты дедлайна, тогда ошибка!
            print(fraza[5])
            return 0
        else:
            stroka_ = str(
                stroka_.strftime("%d.%m.%Y")
                          )                     # Выход из функции с аргументом 0, т.е. нужен повторный ввод
    elif ind_ == 3 and stroka_ not in status_:  # Проверка на вхождение ввода в список статусов заметки
        print(fraza[3])
        return 0                                # Выход из функции с аргументом 0, т.е. нужен повторный ввод статуса
    elif ind_ in [0, 1, 2]:                     # Проверка на ввод имени заметки, заголовка и описания
        for ch in stroka_:
            if ch.isupper(): counter += 1       # Проверка на заглавную букву
            if (counter in [0] and ind_ in
                    [0, 1, 2]):                 # 0 заглавных букв - ошибка
                print(fraza[0])
                return 0                        # Выход из функции с аргументом 0, т.е. нужен повторный ввод
    return stroka_

def replace_dates(match_):                      # Обработка любого ввода даты
    a = []                                      # Список вхождений даты в строке
    b = 0                                       # Временная переменная преобразования даты
    c = ['\\d{2}/\\d{2}/\\d{2,4}', '\\d{2}-\\d{2}-\\d{2,4}',
         '\\d{2}:\\d{2}:\\d{2,4}', '\\d{2}.\\d{2}.\\d{2,4}',
         '\\d{2,4}/\\d{2}/\\d{2}', '\\d{2,4}-\\d{2}-\\d{2}',
         '\\d{2,4}:\\d{2}:\\d{2}', '\\d{2,4}.\\d{2}.\\d{2}']                                   # Список шаблонов даты
    d = ['%d/%m/%Y', '%d-%m-%Y', '%d:%m:%Y',
         '%d.%m.%Y', '%Y/%m/%d', '%Y-%m-%d',
         '%Y:%m:%d', '%Y.%m.%d']                                   # Список форматов вывода даты
    for i, j in zip(c, d):                      # Проверка ввода на наличие в строке даты
        try:
            a = re.findall(i, match_)           # Поиск в строке ввода даты по имеющимся в списке [c] шаблонам
            b = datetime.strptime(a[0], j)      # Преобразование вырезанной строки в тип datetime
            b = datetime.date(b)                # Преобразование datetime в date
            return b                            # Выход из функции с аргументом date
        except:
            continue
    print(fraza[4])                             # Вывод предупреждения об ошибке
    return 0

# Программа
update_note()
