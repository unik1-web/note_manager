from utils.data_entry_function import *

def delete_note(notes_):  # Функция удаления заметки
    counter_del = 0  # Счетчик удаленных заметок
    index_list = 0  # Индекс проверяемого списка заметок
    len_ = len(notes_)
    del_ = data_entry(
        "Введите имя пользователя или заголовок для удаления заметки: ", 1
    )  # Ввод критерия для удаления заметки
    if data_entry(
            "Вы уверены, что хотите удалить заметку? (1да/2нет) ", 6
    ) == 2:
        return
    while (index_list + counter_del) <= len_:
        _dict_ = notes_[index_list]
        for k in range(2):
            if (
                    del_.lower() == _dict_[note_keys[k]].lower()
            ):  # Проверка по критерию с любым регистром ввода
                notes_.remove(_dict_)  # Удаление заметки с искомым критерием
                counter_del += 1
                len_ -= 1
                index_list -= 1
                break
        index_list += 1
    if counter_del == 0:
        print(
            '\033[32m' + "Заметок с таким именем пользователя "
            "или заголовка не найдено."
        )
    else:
        print('\033[32m' + "Успешно удалено.")  # Вывод оставшихся заметок
    return

pass