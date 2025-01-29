# Этап4_Сохранение_Заметок_Юнин_Константин

import yaml

notes = [
    {'username': 'Авдей', 'title': 'Список покупок',
    'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Дормидонт', 'title': 'План учёбы и работы',
     'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Кирилл', 'title': 'План работы',
     'content': 'План работы', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]   # Список словарей заметки
note_end = (
    "Имя пользователя", "Заголовок", "Описание",
    "Статус", "Дата создания", "Дедлайн"
)   # Список элементов заметки для вывода


def append_notes_to_file(notes_, filename):
    values_ = []  # Значения словаря заметок
    copy_notes = []  # Измененная копия списка словарей заметок
    for dikt_ in notes_:
        for values in dikt_.values():
            values_.append(values)
        dikt_chenge = dict(zip(note_end, values_))
        copy_notes.append(dikt_chenge)  # Измененный список считанных словарей заметок
        values_.clear()
    try:
        with open(filename, "a", encoding='UTF-8') as file:
            yaml.dump(copy_notes, file, allow_unicode=True, sort_keys=False)
    except PermissionError:
        print(f"Ошибка прав доступа файла {filename}. Проверьте имя файла или его аттрибуты.")
        return
    print('\033[32m' + "Заметки записаны в файл")


append_notes_to_file(notes, 'data.txt')
