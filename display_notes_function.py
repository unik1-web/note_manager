# Этап3_Финальное_Юнин_Константин.
# Задание 3: Функция отображения заметок
# import pandas as pd

note_states = [
    {'username': 'Алексей', 'title': 'Список покупок',
    'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'План учёбы и работы',
     'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '01-12-2024', 'issue_date': '11-12-2024'},
    {'username': 'Иван', 'title': 'План работы',
     'content': 'План работы', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]       # Список словарей заметки
phrase = {
    0: "Какой вывод заметок предпочитаете? (1Заголовки/2Полные данные) ",
    1: "Сортировать заметки по дате? (1Да/2Нет) ",
    2: "Какой вывод заметок предпочитаете? (1Построчный/2Табличный) ",
    3: "Cортировать заметки по дате создания или дедлайну? 1/2: ",
    4: "Нажмите Enter для продолжения"
}             # Словарь фраз для вывода
note_end = (
    "Имя пользователя: ", "Заголовок: ",
    "Описание: ", "Статус: ",
    "Дата создания: ", "Дедлайн: "
)           # Список элементов заметки для вывода
note_keys = (
    "username", "title", "content", "status",
    "created_date", "issue_date"
)          # Кортеж ключей словаря заметки


def display_notes(notes):
    global data_
    if len(notes) == 0:  # Проверка на наличие заметок
        print("У вас нет сохранённых заметок.")
        return
    data_ = data_entry(phrase[0])
    if data_entry(phrase[1]) == 1:
        notes = sorting_(notes)  # Сортировка списка словарей по дате создания или дедлайну
    # if data_ == 2:
        # outp_ = data_entry(phrase[0])
        # if data_entry(phrase[0]) == 2:
        #     output_tab(notes)  # Вывод заметок в виде таблицы
        #     return
    output_(notes)  # Вывод заметок построчно


def data_entry(stroka_):
    while True:
        if stroka_ == phrase[4]:
            input('\033[39m' +
                  stroka_)  # Изменение цвета текста на стандартный
            # print('\033[32m')           # Изменение цвета текста на зелёный
            return
        else:
            date_ = input(stroka_)
            date_ = check_(date_)
            if date_ == 0:  # Проверка вводимых данных на ошибку
                continue
            else:
                return date_  # Возврат целого числа


def check_(stroka_):  # Проверка вводимых данных
    if stroka_ not in ["1", "2"]:  # Ввод отличается от 1 или 2
        print("Пожалуйста повторите ввод правильно: 1, либо 2!")
        return 0
    else:
        return int(stroka_)  # Возврат целого числа


def sorting_(notes):
    if data_entry(phrase[3]) == 1:      # Сортировка словаря по дате создания или дедлайну
        sorted_list = sorted(note_states, key=lambda x: x["created_date"])
    else:
        sorted_list = sorted(note_states, key=lambda x: x["issue_date"])
    return sorted_list  # Возврат отсортированного списка словарей

def output_(notes):  # Вывод заметок в виде столбца
    print('\033[32m' + 'Список заметок:')  # Изменение цвета текста на зелёный
    print("---------------")
    k = 0
    for l, _dict_ in enumerate(notes):
        if data_ == 2:
            if (l % 5) == 0 and l != 0:
                data_entry(phrase[4])
            print('\033[32m' + 'Заметка №', (l+1), ':')  # Вывод номера заметки
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


# def output_tab(notes):
#     print('Список заметок:')
#     data = notes.values()
#     df = pd.DataFrame(data, columns=note_end)  # Формирование табличного списка
#     print(df)
#     return





# Программа
display_notes(note_states)
print('\033[39m')  # Изменение цвета текста на стандартный
