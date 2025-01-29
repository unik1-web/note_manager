import json


def save_notes_json(notes_, filename):  # Сохраняет заметки в формате JSON
    try:
        with open(filename, 'w', encoding='UTF-8') as f:  # блок для автоматического закрытия файла
            json.dump(notes_, f, indent=4, ensure_ascii=False)
    except PermissionError:
        print(f"Ошибка прав доступа файла {filename}. Проверьте имя файла или его аттрибуты.")
        return
    print('\033[32m' + "Заметки записаны в файл JSON")


pass