

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
                        f'{note_end[i]}'+': '+
                        f'{_dict_[res]}'
                    )  # Вывод заметок по образцу
            else:
                print('\033[32m' + 'Заметка №', (l + 1), ':')  # Вывод номера заметки
                print(
                    f'{note_end[1]}'+': '+
                    f'{list_[l][note_keys[1]]}'  # Вывод заголовков построчно
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