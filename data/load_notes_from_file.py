from interface.data_string_notes import *
import yaml


def load_notes(filename):
    values_ = []  # Значения словаря заметок
    copy_notes = []  # Измененная копия списка словарей заметок
    loaded_data = ''  # Список строк из файла
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            loaded_data = yaml.safe_load(file)
    except UnicodeDecodeError:
        print(f"Ошибка при чтении файла {filename}. Проверьте его содержимое.")
        return
    except FileNotFoundError:
        print(f'Файл {filename} не найден.Создан новый файл.')
        with open(filename, "x", encoding='UTF-8') as file: pass
    if loaded_data in [None]:
        print("Файл заметок пуст.")
        return
    for dikt_ in loaded_data:
        for values in dikt_.values():
            values_.append(values)
        if len(values_) != len(note_keys):
            print(f"Ошибка при чтении файла {filename}. Проверьте его содержимое.")
            return copy_notes
        dikt_chenge = dict(zip(note_keys, values_))  # Измененный словарь заметок после считывания из файла
        copy_notes.append(dikt_chenge)  # Измененный список считанных словарей заметок
        values_.clear()
    print('\033[32m' + "Заметки из файла прочитаны")
    return copy_notes


pass
