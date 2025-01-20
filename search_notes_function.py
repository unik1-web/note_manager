# Этап3_Финальное_Юнин_Константин.
# Задание 4: Функция поиска заметок

note_list = [
    {'username': 'Алексей', 'title': 'Список покупок',
     'content': 'План работы', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},

    {'username': 'Мария', 'title': 'План учёбы и работы',
     'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},

    {'username': 'Иван', 'title': 'План работы',
     'content': 'План работы', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]  # Список словарей заметки
note_end = ("Имя пользователя: ", "Заголовок: ", "Описание: ",
            "Статус: ", "Дата создания: ", "Дедлайн: "
            )  # Список элементов заметки для вывода
phrase = {
    1: "Вы неправильно ввели статус заметки (новая, в процессе, выполнено), повторите ввод!",
    8: "Нажмите Enter для продолжения",
    13: "Вы ввели некорректное значение, пожалуйста повторите ввод!",
    14: "Пожалуйста повторите ввод правильно: либо 1, либо 2!"
}  # Словарь фраз для вывода
status_ = (
    "новая",
    "в процессе",
    "выполнено"
)  # Кортеж статусов заметки для ввода


def search_notes():
    list_of_words = []  # Список ключевых слов для поиска по нескольким словам
    searches = []  # Список найденных по ключевым словам заметок
    status = None  # Статус для поиска заметки

    def search_(keyword=None, stat_=None):
        dikt_ = []  # Список найденных по ключевым словам заметок
        keyword = keyword.lower() if keyword is not None else keyword  # Проверка по критерию с любым регистром ввода
        stat_ = stat_.lower() if stat_ is not None else stat_  # Проверка по критерию с любым регистром ввода
        if len(note_list) == 0:  # Проверка на наличие заметок
            print("\033[32m" + "У вас нет сохранённых заметок.")
            return
        if keyword is None:  # Поиск по статусу
            for sub in note_list:
                for val in sub.values():
                    if stat_ in val:
                        dikt_.append(sub)  # Добавление заметки с критерием в словарь
                        break
        elif stat_ is None:  # Поиск по ключевому слову
            for sub in note_list:
                for val in sub.values():
                    if word_ in val.split():
                        dikt_.append(sub)  # Добавление заметки с критерием в словарь
                        break
        else:
            for sub in note_list:  # Поиск по статусу и ключевому слову
                for val in sub.values():
                    if word_ in val.split():
                        for vals in sub.values():
                            if stat_ in vals:
                                dikt_.append(sub)  # Добавление заметки с критерием в словарь
                                break
                        break
        if len(dikt_) == 0:  # Проверка на наличие заметок, соответствующих критериям
            print("\033[32m" + "Заметки, соответствующие запросу, не найдены.")
            return
        else:
            return dikt_

    while True:
        ind_word = data_entry("\033[39m" + "Хотите ввести ключевое слово для поиска? 1Да/2Нет ", 6)
        if ind_word == 1:
            list_of_words.append(data_entry("Введите ключевое слово: ", 8))
            continue
        ind_status = data_entry("Хотите ввести статус заметки для поиска? 1Да/2Нет ", 6)
        if ind_status == 1:
            status = data_entry("Введите статус заметки для поиска (по умолчанию - новая): ", 3)
        break
    if ind_status == 2 and list_of_words == []:
        return  # Выход из функции при отсутствии ключевых слов и статуса для поиска
    if len(list_of_words) == 0:
        if ind_status == 1:
            searches = search_(stat_=status)  # Поиск по статусу
            if searches is not None: output_(searches)  # Вывод найденных заметок при их наличии
            return
        else:
            return
    else:
        for word_ in list_of_words:  # Поиск по списку слов с формированием списка найденных заметок
            searches = search_(keyword=word_, stat_=status)
    search_list = searches if searches is not None else None
    if search_list is not None:
        output_(search_list)  # Вывод найденных заметок при их наличии
    return


def data_entry(string_, ind_):
    def check_(str_, ind_):  # Проверка вводимых данных
        counter = 0  # Счетчик заглавных букв
        if str_ == "" and ind_ not in [3, 4, 5]:
            print(phrase[13])
            return 0
        if ind_ == 3:
            if str_ == "":  # Пустой ввод создания статуса заметки "новая"
                str_ = "новая"
            elif str_ not in status_:  # Проверка на вхождение ввода в список статусов заметки
                print(phrase[1])
                return 0  # Выход из функции с аргументом 0, т.е. нужен повторный ввод статуса
        elif ind_ == 6:
            if str_ not in ["1", "2"]:  # Ввод отличается от 1 или 2
                print(phrase[14])
                return 0
            else:
                return int(str_)
        return str_

    while True:
        if string_ in [phrase[8]]:
            dates = input(
                '\033[39m' + '\n' + string_
            )  # Изменение цвета текста на стандартный
            return dates
        else:
            dates = input(string_)
            dates = check_(dates, ind_)
            if dates == 0:  # Проверка вводимых данных на ошибку
                continue
            else:
                return dates  # Возврат целого числа


def output_(notes):  # Вывод заметок в виде столбца
    for l, _dict_ in enumerate(notes):
        print('\033[32m' + 'Найдены заметки:')  # Изменение цвета текста на зелёный
        print('\033[32m' + 'Заметка №', (l + 1), ':')  # Вывод номера заметки
        for i, res in enumerate(_dict_.keys()):
            print(f'{note_end[i]}'
                  f'{_dict_[res]}')


# Программа
print("Исходный список заметок: ")
print(note_list)
search_notes()
