def search_notes(notes, keyword, status_):  # Функция поиска заметки
    dikt_ = []
    if keyword is None:  # Поиск по статусу
        for sub in notes:
            for val in sub.values():
                if status_ in val:
                    dikt_.append(sub)  # Добавление заметки с критерием в словарь
                    break
    elif status_ is None:  # Поиск по ключевому слову
        for sub in notes:
            for val in sub.values():
                if keyword in val.split():
                    dikt_.append(sub)  # Добавление заметки с критерием в словарь
                    break
    else:
        for sub in notes:  # Поиск по статусу и ключевому слову
            for val in sub.values():
                if keyword in val.split():
                    for vals in sub.values():
                        if status_ in vals:
                            dikt_.append(sub)  # Добавление заметки с критерием в словарь
                            break
                    break
    if len(dikt_) == 0:  # Проверка на наличие заметок, соответствующих критериям
        print("\033[32m" + "Заметки, соответствующие запросу, не найдены.")
        return
    else:
        print('\033[32m' + 'Найдены заметки:')
        return dikt_
