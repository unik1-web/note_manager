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
)        # Кортеж элементов заметки для ввода
status_ = (
    "новая", "в процессе", "выполнено"
)      # Кортеж статусов заметки для ввода
phrase = {
    0: "Вы ввели текст без заглавной буквы, поэтому повторите ввод!",
    1: "Вы неправильно ввели статус заметки, повторите ввод!",
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
}       # Словарь фраз для вывода
c = [
    '\\d{2}/\\d{2}/\\d{2,4}', '\\d{2}-\\d{2}-\\d{2,4}',
    '\\d{2}:\\d{2}:\\d{2,4}', '\\d{2}.\\d{2}.\\d{2,4}',
    '\\d{2,4}/\\d{2}/\\d{2}', '\\d{2,4}-\\d{2}-\\d{2}',
    '\\d{2,4}:\\d{2}:\\d{2}', '\\d{2,4}.\\d{2}.\\d{2}'
]  # Список шаблонов даты
d = [
    '%d/%m/%Y', '%d-%m-%Y', '%d:%m:%Y',
    '%d.%m.%Y', '%Y/%m/%d', '%Y-%m-%d',
    '%Y:%m:%d', '%Y.%m.%d'
]  # Список форматов вывода даты
note_end = (
    "Имя пользователя: ", "Заголовок: ",
    "Описание: ", "Статус: ",
    "Дата создания: ", "Дедлайн: "
)       # Кортеж элементов заметки для вывода
note_keys = [
    "username", "title", "content",
    "status", "created_date", "issue_date"
]       # Кортеж ключей словаря заметки
note_list = []      # Список словарей заметки
note = []  # Список данных текущей заметки



def create_note():
    note = []
    note_states = {}  # Словарь заметки
    ind_ = 0  # Индекс заполнения списка для словаря заметок
    while ind_ < 6:  # Ввод данных пользователем
        string_ = data_entry(("Введите " + note_[ind_]),ind_)
        note.append(string_)
        ind_ += 1
    # print(note)
    for i, j in zip(note_keys,range(6)):
        note_states[i] = note[j]         # Внесение данных в словарь
    print("\033[32m" + "Новая заметка создана!")
    dict = note_states.copy()
    note_list.append(dict)
    note_states.clear()
    return


def data_entry(string_, ind_):
    while True:
        if string_ in [phrase[8], phrase[15]]:
            data_ = input(
                '\033[39m' + '\n' + string_
            )       # Изменение цвета текста на стандартный
            return data_
        else:
            if ind_ in [4]:
                string_ = str(
                    date.today().strftime("%d.%m.%Y")
                )       # Присвоение словарю текущей даты в формате день.месяц.год
                return string_
            data_ = input(string_)
            if ind_ in [5] and data_ == "":  # Пустой ввод создания статуса заметки "новая"
                string_ = (date.today() + timedelta(weeks=1))  # Присвоение дедлайну даты +7 дней от сегодняшней
                string_ = str(string_.strftime("%d.%m.%Y"))
                return string_
            data_ = check_(data_, ind_)
            if data_ == 0:      # Проверка вводимых данных на ошибку
                continue
            else:
                return data_       # Возврат целого числа


def display_notes(notes):

    def sorting_(notes):
        if data_entry(phrase[7]) == 1:  # Сортировка словаря по дате создания или дедлайну
            notes.sort(key=lambda x: datetime.strptime(x['created_date'], '%d-%m-%Y'))
        else:
            notes.sort(key=lambda x: datetime.strptime(x['issue_date'], '%d-%m-%Y'))
        return notes  # Возврат отсортированного списка словарей

    def output_(notes):  # Вывод заметок в виде столбца
        print('\033[32m' + 'Список заметок:')  # Изменение цвета текста на зелёный
        print("---------------")
        for l, _dict_ in enumerate(notes):
            if data_ == 2:
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
                    f'{notes[l][note_keys[1]]}'
                )
            print("---------------------")

    def output_tab(notes):  # Вывод заметок в виде таблицы
        print('\033[32m' + 'Список заметок:\n')
        print(tabulate(notes, headers='keys'))
        print('\033[39m')
        return

    global data_
    if len(notes) == 0:     # Проверка на наличие заметок
        print("У вас нет сохранённых заметок.")
        return
    data_ = data_entry(phrase[4], 6)
    if data_entry(phrase[5], 6) == 1:
        notes = sorting_(notes)     # Сортировка списка словарей по дате создания или дедлайну
    if data_ == 2:
        if data_entry(phrase[6], 6) == 2:
            output_tab(notes)       # Вывод заметок в виде таблицы
            return
    output_(notes)          # Вывод заметок построчно


def update_note():
    global data_entr, note_field
    num_= data_entry("Введите номер обновляемой заметки: ", 7)
    note_states = note_list[int(num_)-1]
    while True:
        data_entr = data_entry(phrase[9], 8)
        if data_entr in note_keys:
            while True:
                note_field = input(phrase[10] + data_entr + " : ")
                che_ = check_(
                    note_field, note_keys.index(data_entr)
                                )       # Проверка вводимых данных
                if che_ == 0:
                    continue      # Выход из цикла для повторного ввода
                else:
                    if data_entry(phrase[11], 6) in [1]:       # Проверка на необходимость изменения словаря
                        note_states[data_entr] = che_       # Изменение словаря заметки по ключу
                        print("Заметка обновлена: ")
                    else:
                        print("Заметка не обновлена!")
                    return
        else:
            print(phrase[13])
            continue


def check_(string_, ind_):  # Проверка вводимых данных
    counter = 0  # Счетчик заглавных букв
    if string_ == "" and ind_ not in [3,4,5]: return 0
    if ind_ in [5]:
        string_ = replace_dates(string_)  # Проверка на ввод даты и преобразование в тип datetime
        if string_ == 0:
            print(phrase[2])
            return 0  # Данные не прошли проверку. Выход из функции с аргументом 0
        else:
            note.append(str(string_.strftime("%d.%m.%Y")))  # Присвоение словарю текущей даты в формате день.месяц.год
        if ind_ in [5] and (
                string_ - date.today()
        ).days <= 0:  # Дата создания меньше или равна даты дедлайна, тогда ошибка!
            print(phrase[3])
            return 0
        else:
            string_ = str(
                string_.strftime("%d.%m.%Y")
            )  # Выход из функции с аргументом 0, т.е. нужен повторный ввод
    elif ind_ == 3:
        if string_ == "":   # Пустой ввод создания статуса заметки "новая"
            string_ = "новая"
        elif string_ not in status_:  # Проверка на вхождение ввода в список статусов заметки
            print(phrase[1])
            return 0  # Выход из функции с аргументом 0, т.е. нужен повторный ввод статуса
    elif ind_ in [0, 1, 2]:  # Проверка на ввод имени заметки, заголовка и описания
        for ch in string_:
            if ch.isupper(): counter += 1  # Проверка на заглавную букву
            if (counter in [0] and ind_ in
                    [0, 1, 2]):  # 0 заглавных букв - ошибка
                print(phrase[0])
                return 0  # Выход из функции с аргументом 0, т.е. нужен повторный ввод
    elif ind_ == 6:
        if string_ not in ["1", "2"]:  # Ввод отличается от 1 или 2
            print(phrase[14])
            return 0
        else:
            return int(string_)
    elif ind_ == 7:
        if not string_.isdigit():
            return 0
    return string_


def replace_dates(match_):  # Обработка любого ввода даты
    a = []  # Список вхождений даты в строке
    b = 0  # Временная переменная преобразования даты
    for i, j in zip(c, d):  # Проверка ввода на наличие в строке даты
        try:
            a = re.findall(i, match_)  # Поиск в строке ввода даты по имеющимся в списке [c] шаблонам
            b = datetime.strptime(a[0], j)  # Преобразование вырезанной строки в тип datetime
            b = datetime.date(b)  # Преобразование datetime в date
            return b  # Выход из функции с аргументом date
        except:
            continue
    print(phrase[4])  # Вывод предупреждения об ошибке
    return 0


def delete_note():
    m = 0       # Счетчик удаленных заметок
    l = 0       # Индекс проверяемого списка заметок
    len_= len(note_list)
    del_ = data_entry(
        "Введите имя пользователя или заголовок для удаления заметки: ", 1
    )       # Ввод критерия для удаления заметки
    if data_entry(
            "Вы уверены, что хотите удалить заметку? (1да/2нет) ", 6
    ) == 2:
        return
    while (l + m) <= len_:
        _dict_ = note_list[l]
        for k in range(2):
            if (
            del_.lower() == _dict_[note_keys[k]].lower()
            ):       # Проверка по критерию с любым регистром ввода
                note_list.remove(_dict_)         # Удаление заметки с искомым критерием
                m += 1
                len_ -= 1
                l -= 1
                break
        l += 1
    if m == 0:
        print('\033[32m' + "Заметок с таким именем пользователя или заголовка не найдено.")
    else:
        print('\033[32m' + "Успешно удалено.")           # Вывод оставшихся заметок
    return


# Programm
while True:
    print("\033[32m" + "Меню действий:")
    print("1. Создать новую заметку")
    print("2. Показать все заметки")
    print("3. Обновить заметку")
    print("4. Удалить заметку")
    print("5. Найти заметки")
    print("6. Выйти из программы")
    data_untry = input("\033[39m" + "Ваш выбор: ")
    if data_untry.isdigit():
        data_untry = int(data_untry)
    else:
        continue
    if data_untry in [1]:
        create_note()
        continue
    elif data_untry in [2]:
        display_notes(note_list)
    elif data_untry in [3]:
        update_note()
    elif data_untry in [4]:
        delete_note()
    elif data_untry in [6]:
        print("\033[32m" + "Программа завершена. Спасибо за использование!")
        print("\033[39m")
        break
    else:
        print("\033[32m" + "Неверный выбор. Пожалуйста, выберите действие из списка.")
        continue
