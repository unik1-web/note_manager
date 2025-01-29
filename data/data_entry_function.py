

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

