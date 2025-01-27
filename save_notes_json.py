# Этап4_JSON_Формат_Заметок_Юнин_Константин

import json

notes = [
    {'username': 'Алексей', 'title': 'Список покупок',
    'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'План учёбы и работы',
     'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы',
     'content': 'План работы', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]   # Список словарей заметки


def save_notes_json(notes_, filename):  # Сохраняет заметки в формате JSON
    try:
        with open(filename, 'w', encoding='UTF-8') as f:  # блок для автоматического закрытия файла
            json.dump(notes_, f, indent=4, ensure_ascii=False)
    except PermissionError:
        print(f"Ошибка прав доступа файла {filename}. Проверьте имя файла или его аттрибуты.")
        return
    print('\033[32m' + "Заметки записаны в файл JSON")


save_notes_json(notes, 'notes.json')
