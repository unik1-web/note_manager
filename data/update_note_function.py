

def update_note(note_states):   # Функция обновления данных заметки
    while True:
        data_entr = data_entry(phrase[9], 8)
        if data_entr in note_keys:
            dat_ = data_entry((phrase[10] + data_entr + ": "), note_keys.index(data_entr))
            if data_entry(phrase[11], 6) in [1]:  # Проверка на необходимость изменения словаря
                note_states[data_entr] = dat_  # Изменение словаря заметки по ключу
                print("Заметка обновлена: ")
                return note_states
            return
        else:
            print(phrase[13])
            continue