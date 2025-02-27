import yaml
from interface.data_string_notes import *


def save_notes_file(notes_, filename):
    values_ = [] # Значения словаря заметок
    copy_notes = []  # Измененная копия списка словарей заметок
    for dikt_ in notes_:
        for values in dikt_.values():
            values_.append(values)
        d = dict(zip(note_end, values_)) # Измененный словарь заметок
        copy_notes.append(d)
        values_.clear()
    try:
        with open(filename, "w", encoding='UTF-8') as file:
            yaml.dump(copy_notes, file, allow_unicode=True, sort_keys=False)
    except PermissionError:
        print(f"Ошибка прав доступа файла {filename}. Проверьте имя файла или его аттрибуты.")
        return
    print('\033[32m' + "Заметки записаны в файл !")

pass