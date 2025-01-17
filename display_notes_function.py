# Этап3_Финальное_Юнин_Константин.
# Задание 3: Функция отображения заметок
# import pandas as pd

note_states = [
    {'username': 'Алексей', 'title': 'Список покупок',
    'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'План учёбы и работы',
     'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы',
     'content': 'План работы', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]       # Список словарей заметки
phrase = {0: "Какой вывод заметок предпочитаете? (1 Заголовки/2 Полные данные) ",
          1: "Сортировать заметки по дате? (1 Да/2 Нет) ",
          2: "Какой вывод заметок предпочитаете? (1 Построчный/2 Табличный) ",
          3: "Вы неправильно ввели статус заметки,(новая, в процессе, выполнено), поэтому повторите ввод!",
          4: "Неверный формат даты. Пожалуйста, убедитесь, что дата введена правильно.",
          5: "Дата дедлайна не может быть раньше даты создания заметки, повторите ввод!"}                                   # Словарь фраз для вывода

note_end = ("Имя пользователя: ", "Заголовок: ", "Описание: ", "Статус: ",
            "Дата создания: ", "Дедлайн: "
            )  # Список элементов заметки для вывода
# note_states = []

def display_notes(notes):
    global data_
    if len(notes) == 0:  # Проверка на наличие заметок
        print("У вас нет сохранённых заметок.")
        return
    data_ = data_entry(phrase[0])
    sort_ = data_entry(phrase[1])
    if sort_ == 1:
        notes = sorting(notes)  # Сортировка словаря по дате создания или дедлайну
    if data_ == 2:
        outp_ = data_entry(phrase[0])
        if outp_ == 2:
            output_tab(notes)  # Вывод заметок в виде таблицы
            return
    output_(notes)  # Вывод заметок построчно


def output_(notes):  # Вывод заметок в виде столбца
    print('\033[32m' + 'Список заметок:')  # Изменение цвета текста на зелёный
    print("---------------")
    k = 0
    for i in notes.keys():
        k += 1
        if data_ == 2:
            if ((k - 1) % 5) == 0 and (k - 1) != 0:
                data_entry('Нажмите Enter для продолжения')
            print('\033[32m' + 'Заметка №', k, ':')  # Вывод номера заметки
            for j in range(6):  # Вывод заметок построчно
                print(f'{note_end[j]}'
                      f'{notes[i][j]}')
        else:
            print(f'{note_end[1]}'  # Вывод заголовков построчно
                  f'{notes[i][1]}')
        print("---------------")


def proverka(stroka_):  # Проверка вводимых данных
    if stroka_ not in ["1", "2"]:  # Ввод отличается от 1 или 2
        print("Пожалуйста повторите ввод правильно: либо 1, либо 2!")
        return 0
    else:
        return int(stroka_)  # Возврат целого числа


def sorting(notes):
    sort = data_entry("Cортировать заметки по дате создания или дедлайну? 1/2: ")
    sorted_notes = {
        key: value
        for key, value in sorted(notes.items(),
                                 key=lambda item: item[1][sort + 3])
                    }  # Сортировка словаря по дате создания или дедлайну
    return sorted_notes  # Возврат отсортированного словаря


def output_tab(notes):
    print('Список заметок:')
    data = notes.values()
    df = pd.DataFrame(data, columns=note_end)  # Формирование табличного списка
    print(df)
    return


def data_entry(stroka_):
    while True:
        if stroka_ == "Нажмите Enter для продолжения":
            input('\033[39m' +
                  stroka_)  # Изменение цвета текста на стандартный
            # print('\033[32m')           # Изменение цвета текста на зелёный
            return
        else:
            vvod_ = input(stroka_)
            vvod_ = proverka(vvod_)
            if vvod_ == 0:  # Проверка вводимых данных на ошибку
                continue
            else:
                return vvod_  # Возврат целого числа


# Программа
display_notes(note_states)
print('\033[39m')  # Изменение цвета текста на стандартный
