# Этап3_Финальное_Юнин_Константин.
# Собрать и организовать результаты всех задач этапа 3 в одном проекте,
# чтобы продемонстрировать навыки работы с функциями, улучшить структурированность кода и
# упростить взаимодействие пользователя с системой управления заметками.

import re
from datetime import date, datetime, timedelta
from tabulate import tabulate

note_ = (
    "имя пользователя: ",
    "заголовок заметки: ",
    "описание заметки: ",
    "статус заметки (новая, в процессе, выполнено. По умолчанию новая): ",
    "",
    "дату дедлайна (в любом формате или 7 дней от текущей даты по умолчанию):"
)  # Кортеж элементов заметки для ввода
status_ = (
    "новая",
    "в процессе",
    "выполнено"
)  # Кортеж статусов заметки для ввода
phrase = {
    0: "Вы ввели текст без заглавной буквы, поэтому повторите ввод!",
    1: "Вы неправильно ввели статус заметки (новая, в процессе, выполнено), повторите ввод!",
    2: "Неверный формат даты. Пожалуйста, убедитесь, что дата введена правильно.",
    3: "Дата дедлайна не может быть раньше даты создания заметки, повторите ввод!",
    4: "Какой вывод заметок предпочитаете? (1Заголовки/2Полные данные) ",
    5: "Сортировать заметки по дате? (1Да/2Нет) ",
    6: "Какой вывод заметок предпочитаете? (1Построчный/2Табличный) ",
    7: "Cортировать заметки по дате создания или дедлайну? 1/2: ",
    8: "Нажмите Enter для продолжения",
    9: "Какие данные вы хотите обновить? (username, title, content, status, issue_date): ",
    10: "Введите новое значение для ",
    11: "Вы уверены, что хотите обновить поле? (1да/2нет) ",
    12: "Вы хотите продолжить? (1да/2нет) ",
    13: "Вы ввели некорректное значение, пожалуйста повторите ввод!",
    14: "Пожалуйста повторите ввод правильно: либо 1, либо 2!",
    15: "Введите ключевое слово: "
}  # Словарь фраз для вывода
pattern_date = [
    '\\d{2}/\\d{2}/\\d{2,4}', '\\d{2}-\\d{2}-\\d{2,4}',
    '\\d{2}:\\d{2}:\\d{2,4}', '\\d{2}.\\d{2}.\\d{2,4}',
    '\\d{2,4}/\\d{2}/\\d{2}', '\\d{2,4}-\\d{2}-\\d{2}',
    '\\d{2,4}:\\d{2}:\\d{2}', '\\d{2,4}.\\d{2}.\\d{2}'
]  # Список шаблонов даты
date_output_format = [
    '%d/%m/%Y', '%d-%m-%Y', '%d:%m:%Y',
    '%d.%m.%Y', '%Y/%m/%d', '%Y-%m-%d',
    '%Y:%m:%d', '%Y.%m.%d'
]  # Список форматов вывода даты
note_end = (
    "Имя пользователя: ", "Заголовок: ",
    "Описание: ", "Статус: ",
    "Дата создания: ", "Дедлайн: "
)  # Кортеж элементов заметки для вывода
note_keys = [
    "username", "title", "content",
    "status", "created_date", "issue_date"
]  # Кортеж ключей словаря заметки
notes = []  # Список словарей заметки
note = {}  # Словарь заметки
found_notes = None


def create_note():  # Функция ввода данных заметки
    notes_ = []  # Список заметки
    note_states = {}  # Словарь заметки
    ind_ = 0  # Индекс заполнения списка для словаря заметок
    while ind_ < 6:  # Ввод данных пользователем
        string_ = data_entry(("Введите " + note_[ind_]), ind_)
        notes_.append(string_)
        ind_ += 1
    for key, j in zip(note_keys, range(6)):
        note_states[key] = notes_[j]  # Внесение данных в словарь
    print("\033[32m" + "Новая заметка создана!")
    return note_states


def display_notes(note_list): # Функция вывода данных заметки
    def sorting_(notes_):
        if data_entry(phrase[7]) == 1:  # Сортировка словаря по дате создания или дедлайну
            notes_.sort(key=lambda x: datetime.strptime(x['created_date'], '%d-%m-%Y'))
        else:
            notes_.sort(key=lambda x: datetime.strptime(x['issue_date'], '%d-%m-%Y'))
        return notes_  # Возврат отсортированного списка словарей

    def output_(list_, date_=2):  # Вывод заметок в виде столбца
        print('\033[32m' + 'Список заметок:')  # Изменение цвета текста на зелёный
        print("---------------")
        for l, _dict_ in enumerate(list_):
            if date_ == 2:
                if (l % 5) == 0 and l != 0:
                    data_entry(phrase[8])
                print('\033[32m' + 'Заметка №', (l + 1), ':')  # Вывод номера заметки
                for i, res in enumerate(_dict_.keys()):
                    print(
                        f'{note_end[i]}'
                        f'{_dict_[res]}'
                    )  # Вывод заметок по образцу
            else:
                print('\033[32m' + 'Заметка №', (l + 1), ':')  # Вывод номера заметки
                print(
                    f'{note_end[1]}'  # Вывод заголовков построчно
                    f'{list_[l][note_keys[1]]}'
                )
            print("---------------------")

    def output_tab(list__):  # Вывод заметок в виде таблицы
        list_ = list__.copy()    # копия списка для вывода
        for i, mydict in enumerate(list_):
            pos = list(mydict.keys()).index('username')
            items = list(mydict.items())
            items.insert(
                pos, ('№', i+1)
            )  # Вставка в каждый словарь ключа "№" для нумерации заметок в таблице
            list_[i] = dict(items)
        print('\033[32m' + 'Список заметок:\n')
        print(tabulate(list_, headers='keys'))
        print('\033[39m')
        return

    dates_ = data_entry('\033[39m' + phrase[4], 6)  # Выбор: заголовки или полные данные?
    if data_entry(phrase[5], 6) == 1:
        note_list = sorting_(note_list)  # Сортировка списка словарей по дате создания или дедлайну
    if dates_ == 2:
        if data_entry(phrase[6], 6) == 2:
            output_tab(note_list)  # Вывод заметок в виде таблицы
            return
    output_(note_list, dates_)  # Вывод заметок построчно


def update_note(note_states):   # Функция обновления данных заметки
    while True:
        data_entr = data_entry(phrase[9], 8)
        if data_entr in note_keys:
            dat_ = data_entry((phrase[10] + data_entr + ": "), note_keys.index(data_entr))
            if data_entry(phrase[11], 6) in [1]:  # Проверка на необходимость изменения словаря
                note_states[data_entr] = dat_  # Изменение словаря заметки по ключу
                print("Заметка обновлена: ")
                return note_states
            return
        else:
            print(phrase[13])
            continue


def delete_note():  # Функция удаления заметки
    counter_del = 0  # Счетчик удаленных заметок
    index_list = 0  # Индекс проверяемого списка заметок
    len_ = len(notes)
    del_ = data_entry(
        "Введите имя пользователя или заголовок для удаления заметки: ", 1
    )  # Ввод критерия для удаления заметки
    if data_entry(
            "Вы уверены, что хотите удалить заметку? (1да/2нет) ", 6
    ) == 2:
        return
    while (index_list + counter_del) <= len_:
        _dict_ = notes[index_list]
        for k in range(2):
            if (
                    del_.lower() == _dict_[note_keys[k]].lower()
            ):  # Проверка по критерию с любым регистром ввода
                notes.remove(_dict_)  # Удаление заметки с искомым критерием
                counter_del += 1
                len_ -= 1
                index_list -= 1
                break
        index_list += 1
    if counter_del == 0:
        print('\033[32m' + "Заметок с таким именем пользователя или заголовка не найдено.")
    else:
        print('\033[32m' + "Успешно удалено.")  # Вывод оставшихся заметок
    return


def search_notes(notes, keyword, status_):  # Функция поиска заметки
    dikt_ = []
    if keyword is None:  # Поиск по статусу
        for sub in notes:
            for val in sub.values():
                if status_ in val:
                    dikt_.append(sub)  # Добавление заметки с критерием в словарь
                    break
    elif status_ is None:  # Поиск по ключевому слову
        for sub in notes:
            for val in sub.values():
                if keyword in val.split():
                    dikt_.append(sub)  # Добавление заметки с критерием в словарь
                    break
    else:
        for sub in notes:  # Поиск по статусу и ключевому слову
            for val in sub.values():
                if keyword in val.split():
                    for vals in sub.values():
                        if status_ in vals:
                            dikt_.append(sub)  # Добавление заметки с критерием в словарь
                            break
                    break
    if len(dikt_) == 0:  # Проверка на наличие заметок, соответствующих критериям
        print("\033[32m" + "Заметки, соответствующие запросу, не найдены.")
        return
    else:
        print('\033[32m' + 'Найдены заметки:')
        return dikt_


def data_entry(string_, ind_=7):    # Функция проверки ввода данных заметки
    def check_(str_, ind_):  # Проверка вводимых данных
        counter = 0  # Счетчик заглавных букв
        if str_ == "" and ind_ not in [3, 4, 5, 8]:
            print(phrase[13])
            return 0
        if ind_ in [5]:
            str_ = replace_dates(str_)  # Проверка на ввод даты и преобразование в тип datetime
            if str_ == 0:
                print(phrase[2])
                return 0  # Данные не прошли проверку. Выход из функции с аргументом 0
            if ind_ in [5] and (
                    str_ - date.today()
            ).days <= 0:  # Дата создания меньше или равна даты дедлайна, тогда ошибка!
                print(phrase[3])
                return 0
            else:
                str_ = str(
                    str_.strftime("%d.%m.%Y")
                )  # Выход из функции с аргументом 0, т.е. нужен повторный ввод
        elif ind_ == 3:
            if str_ == "":  # Пустой ввод создания статуса заметки "новая"
                str_ = "новая"
            elif str_ not in status_:  # Проверка на вхождение ввода в список статусов заметки
                print(phrase[1])
                return 0  # Выход из функции с аргументом 0, т.е. нужен повторный ввод статуса
        elif ind_ in [0, 1, 2]:  # Проверка на ввод имени заметки, заголовка и описания
            for ch in str_:
                if ch.isupper(): counter += 1  # Проверка на заглавную букву
                if (counter in [0] and ind_ in
                        [0, 1, 2]):  # 0 заглавных букв - ошибка
                    print(phrase[0])
                    return 0  # Выход из функции с аргументом 0, т.е. нужен повторный ввод
        elif ind_ == 6:
            if str_ not in ["1", "2"]:  # Ввод отличается от 1 или 2
                print(phrase[14])
                return 0
            else:
                return int(str_)
        elif ind_ == 7:
            if not str_.isdigit():  # Проверка ввода данных на наличие цифр
                return 0
        return str_

    def replace_dates(match_):  # Обработка любого ввода даты
        for i, j in zip(pattern_date, date_output_format):  # Проверка ввода на наличие в строке даты
            try:
                list_string = re.findall(i, match_)  # Поиск в строке ввода даты по имеющимся в списке [pattern_date] шаблонам
                dates = datetime.strptime(list_string[0], j)  # Преобразование вырезанной строки в тип datetime
                dates = datetime.date(dates)  # Преобразование datetime в date
                return dates  # Выход из функции с аргументом date
            except:
                continue
        return 0

    while True:
        if string_ in [phrase[8]]:
            dates = input(
                '\033[39m' + '\n' + string_
            )  # Изменение цвета текста на стандартный
            return dates
        else:
            if ind_ in [4]:
                string_ = str(
                    date.today().strftime("%d.%m.%Y")
                )  # Присвоение словарю текущей даты в формате день.месяц.год
                return string_
            dates = input(string_)
            if ind_ in [5] and dates == "":  # Пустой ввод
                string_ = (date.today() + timedelta(weeks=1))  # Присвоение дедлайну даты +7 дней от сегодняшней
                string_ = str(string_.strftime("%d.%m.%Y"))
                return string_
            dates = check_(dates, ind_)
            if dates == 0:  # Проверка вводимых данных на ошибку
                continue
            else:
                return dates  # Возврат целого числа


# Programm
while True:
    print("\033[32m", end="")
    print("""Меню действий:
1. Создать новую заметку
2. Показать все заметки
3. Обновить заметку
4. Удалить заметку
5. Найти заметки
6. Выйти из программы""")
    choice = input("\033[39m" + "Ваш выбор: ")
    if choice.isdigit():
        choice = int(choice)
    else:
        continue
    if choice in [6]:
        print(
            "\033[32m" + "Программа завершена. Спасибо за использование!"
        )
        print("\033[39m")
        break
    elif choice in [1]:
        note = create_note()
        notes.append(note)
    elif len(notes) == 0 and choice in [2, 3, 4, 5]:
        print("Список заметок пуст.")
        continue
    elif choice in [2]:
        display_notes(notes)
    elif choice in [3]:
        display_notes(notes)
        index = int(data_entry("\033[39m"+"Введите номер заметки для обновления: "))-1
        if 0 <= index < len(notes):
            notes[index] = update_note(notes[index])
        else:
            print("Неверный номер заметки.")
    elif choice in [4]:
        delete_note()
    elif choice in [5]:
        keyword = data_entry("\033[39m"+"Введите ключевое слово для поиска: ",8)
        status = data_entry("\033[39m"+"Введите статус для поиска (или оставьте пустым): ",8)
        found_notes = search_notes(notes, keyword, status)
        if found_notes is not None: display_notes(found_notes)
    else:
        print(
            "\033[39m" + "Неверный выбор. Пожалуйста, выберите действие из списка."
        )
        continue
        break
