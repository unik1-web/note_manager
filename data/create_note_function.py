from utils.data_entry_function import *


def create_note():  # Функция ввода данных заметки
    notes_ = []  # Список заметки
    note_states = {}  # Словарь заметки
    ind_ = 0  # Индекс заполнения списка для словаря заметок
    while ind_ < 6:  # Ввод данных пользователем
        string_ = data_entry(("Введите " + note_[ind_]), ind_)
        notes_.append(string_)
        ind_ += 1
    for key, j in zip(note_keys, range(6)):
        note_states[key] = notes_[j]  # Внесение данных в словарь
    print("\033[32m" + "Новая заметка создана!")
    return note_states

pass