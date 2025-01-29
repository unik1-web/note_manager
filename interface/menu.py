from data.create_note_function import create_note
from interface.display_note_function import display_notes
from data.update_note_function import update_note
from data.delete_note_function import delete_note
from data.search_note_function import search_notes
from utils.data_entry_function import data_entry
from data.save_notes_to_file import save_notes_file
from data.load_notes_from_file import load_notes
from data.append_notes_to_file import append_notes
from data.save_notes_json import save_notes_json


def menu():
    notes = []  # Список словарей заметки
    found_notes = []
    while True:
        print("\033[32m", end="")
        print("""Меню действий:
    1. Создать новую заметку
    2. Показать все заметки
    3. Обновить заметку
    4. Удалить заметку
    5. Найти заметки
    6. Запись в файл
    7. Добавление данных в файл
    8. Чтение из файла 
    9. Запись в формате JSON
    10. Выйти из программы""")
        choice = input("\033[39m" + "Ваш выбор: ")
        if choice.isdigit():
            choice = int(choice)
        else:
            continue
        if notes == None: notes = []
        if choice in [10]:
            print(
                "\033[32m" + "Программа завершена. Спасибо за использование!"
            )
            print("\033[39m")
            break
        elif choice in [1]:
            notes.append(create_note())
        elif len(notes) == 0 and choice in [2, 3, 4, 5, 6, 7, 9]:
            print("Список заметок пуст.")
            continue
        elif choice in [2]:
            display_notes(notes)
        elif choice in [3]:
            display_notes(notes)
            index = int(data_entry("\033[39m"+"Введите номер заметки для обновления: "))-1
            if 0 <= index < len(notes):
                notes[index] = update_note(notes[index])
            else:
                print("Неверный номер заметки.")
        elif choice in [4]:
            delete_note(notes)
        elif choice in [5]:
            keyword = data_entry("\033[39m"+"Введите ключевое слово для поиска: ",8)
            status = data_entry("\033[39m"+"Введите статус для поиска (или оставьте пустым): ",8)
            found_notes = search_notes(notes, keyword, status)
            if len(found_notes ) != 0: display_notes(found_notes)
        elif choice in [6]:
            save_notes_file(notes, 'data.yml')
        elif choice in [7]:
            append_notes(notes, 'data.yml')
        elif choice in [8]:
            notes = load_notes('data.yml')
        elif choice in [9]:
            save_notes_json(notes, 'data.json')
        else:
            print(
                "\033[39m" + "Неверный выбор. Пожалуйста, выберите действие из списка."
            )
            continue
            break

pass
