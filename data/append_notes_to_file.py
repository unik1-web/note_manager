# Этап4_Сохранение_Заметок_Юнин_Константин

import yaml

notes = []   # Список словарей заметки
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

if __name__ == '__main__':
    append_notes_to_file(notes, 'data.txt')
