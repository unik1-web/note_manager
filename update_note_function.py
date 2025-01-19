# Этап3_Финальное_Юнин_Константин.
# Задание 2: Функция обновления заметки
import re
from datetime import date, datetime

note_states = {
    'username': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты на неделю',
    'status': 'новая',
    'created_date': '10.01.2025',
    'issue_date': '17.01.2025'
}      # Словарь заметки
note = [
    'username', 'title', 'content',
    'status', 'created_date', 'issue_date'
]       # Список ключей словаря заметки
status_ = ("новая", "в процессе", "выполнено")      # Список статусов заметки для ввода
phrase = {
    0: "Вы ввели текст без заглавной буквы, поэтому повторите ввод!",
    1: "Какие данные вы хотите обновить? (username, title, content, status, issue_date): ",
    2: "Введите новое значение для ",
    3: "Вы неправильно ввели статус заметки,(новая, в процессе, выполнено), поэтому повторите ввод!",
    4: "Неверный формат даты. Пожалуйста, убедитесь, что дата введена правильно.",
    5: "Дата дедлайна не может быть раньше даты создания заметки, повторите ввод!",
    6: "Вы уверены, что хотите обновить поле? (1да/2нет) ",
    7: "Вы хотите продолжить? (1да/2нет) ",
    8: "Пожалуйста повторите ввод правильно: либо 1, либо 2!",
    9: "Вы ввели некорректное значение, пожалуйста повторите ввод!"
}          # Словарь фраз для вывода


def update_note():
    global data_entr, note_field
    print("Текущие данные заметки: ")
    print(note_states)
    while True:
        data_entr = input(phrase[1])
        if data_entr in note:
            while True:
                note_field = input(phrase[2] + data_entr + " : ")
                che_ = check_(
                    note_field, note.index(data_entr)
                                )       # Проверка вводимых данных
                if che_ == 0:
                    continue      # Выход из цикла для повторного ввода
                else:
                    if data_entry2(phrase[6]) in [1]:       # Проверка на необходимость изменения словаря
                        note_states[data_entr] = che_       # Изменение словаря заметки по ключу
                        print("Заметка обновлена: ")
                        print(note_states)
                    else:
                        print("Заметка не обновлена!")
                    if data_entry2(phrase[7]) not in [1]:        # Проверка на необходимость изменения словаря
                        return
                    else: break
        else:
            print(phrase[9])
            continue

def check_(string_, ind_):       # Проверка вводимых данных
    counter = 0            # Счетчик заглавных букв
    if string_ == "": return 0
    if ind_ in [4, 5]:
        string_ = replace_dates(string_)        # Проверка на ввод даты и преобразование в тип datetime
        if string_ == 0:
            return 0            # Данные не прошли проверку. Выход из функции с аргументом 0
        if ind_ in [5] and (
                string_ - date.today()
                            ).days <= 0:        # Дата создания меньше или равна даты дедлайна, тогда ошибка!
            print(phrase[5])
            return 0
        else:
            string_ = str(
                string_.strftime("%d.%m.%Y")
                          )                     # Выход из функции с аргументом 0, т.е. нужен повторный ввод
    elif ind_ == 3 and string_ not in status_:  # Проверка на вхождение ввода в список статусов заметки
        print(phrase[3])
        return 0                                # Выход из функции с аргументом 0, т.е. нужен повторный ввод статуса
    elif ind_ in [0, 1, 2]:                     # Проверка на ввод имени заметки, заголовка и описания
        for ch in string_:
            if ch.isupper(): counter += 1       # Проверка на заглавную букву
            if (counter in [0] and ind_ in
                    [0, 1, 2]):                 # 0 заглавных букв - ошибка
                print(phrase[0])
                return 0                        # Выход из функции с аргументом 0, т.е. нужен повторный ввод
    return string_

def data_entry2(string_):
    while True:
        inp_ = input(string_)
        inp_ = check2(inp_)         # Проверка вводимых данных на ошибку
        if inp_ == 0:
            continue
        else:
            return inp_    # Возврат целого числа


def check2(string_):     # Проверка вводимых данных
    if string_ not in ["1", "2"]:       # Ввод отличается от 1 или 2
        print(phrase[8])
        return 0
    else:
        return int(string_)       # Возврат целого числа


def replace_dates(match_):       # Обработка любого ввода даты
    a = []         # Список вхождений даты в строке
    b = 0         # Временная переменная преобразования даты
    c = [
        '\\d{2}/\\d{2}/\\d{2,4}', '\\d{2}-\\d{2}-\\d{2,4}',
        '\\d{2}:\\d{2}:\\d{2,4}', '\\d{2}.\\d{2}.\\d{2,4}',
        '\\d{2,4}/\\d{2}/\\d{2}', '\\d{2,4}-\\d{2}-\\d{2}',
        '\\d{2,4}:\\d{2}:\\d{2}', '\\d{2,4}.\\d{2}.\\d{2}'
    ]          # Список шаблонов даты
    d = [
        '%d/%m/%Y', '%d-%m-%Y', '%d:%m:%Y',
        '%d.%m.%Y', '%Y/%m/%d', '%Y-%m-%d',
        '%Y:%m:%d', '%Y.%m.%d'
    ]          # Список форматов вывода даты
    for i, j in zip(c, d):        # Проверка ввода на наличие в строке даты
        try:
            a = re.findall(i, match_)        # Поиск в строке ввода даты по имеющимся в списке [c] шаблонам
            b = datetime.strptime(a[0], j)      # Преобразование вырезанной строки в тип datetime
            b = datetime.date(b)         # Преобразование datetime в date
            return b          # Выход из функции с аргументом date
        except:
            continue
    print(phrase[4])          # Вывод предупреждения об ошибке
    return 0


# Программа
update_note()