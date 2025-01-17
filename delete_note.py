# Этап2_Финальное_Юнин_Константин.
# Удаление заметок

note_list = [
    {'username': 'Алексей', 'title': 'Список покупок',
    'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Иван', 'title': 'План учёбы и работы',
     'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Алексей', 'title': 'План работы',
     'content': 'План работы', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]         # Список словарей заметки
note_end = (
    "Имя: ", "Заголовок: ",
    "Описание: ", "Статус: ",
    "Дата создания: ", "Дедлайн: "
)          # Список элементов заметки для вывода
output_tab = (
    "\t", "\t\t", "\t\t",
    "\t\t", "\t\t", "\t\t"
)          # Список табуляции элементов заметки для вывода
note_keys = (
    "username", "title", "content", "status",
    "created_date", "issue_date"
)          # Кортеж ключей словаря заметки
note_states = {}        # Словарь текущей заметки

def delete_note(del_):
    del_z = 0        # Счетчик удаленных заметок
    sum_z = len(note_list)      # Количество заметок в списке
    ind_z = -1        # Индекс заметки в списке
    while ind_z < sum_z:
        ind_z += 1
        if ind_z == len(note_list): break
        note_states = note_list[ind_z].copy()      # Словарь из списка заметки копируется в словарь текущей заметки
        for i in range(2):       # Проверка критерия по имени и заголовку
            if (
            del_.lower() == note_states[note_keys[i]].lower()
            ) :         # Проверка по критерию с любым регистром ввода
                del note_list[ind_z]        # Удаление заметки с искомым критерием
                del_z += 1
                ind_z -= 1
                sum_z -= 1
                break
        continue
    if del_z == 0:
        print("Заметок с таким именем пользователя или заголовком не найдено.")
    else:
        print("Успешно удалено. Остались следующие заметки:")
        output(note_list)       # Вывод оставшихся заметок
    return


def output(notes):     # Вывод заметок в виде столбца
    if len(notes) == 0:
        print("Заметки отсутствуют.")
        return
    for i, dict_ in enumerate(note_list):
        print((i + 1), '.', end="")      # Вывод номера заметки
        for j, res in enumerate(dict_.keys()):
            print(f'{output_tab[j]}'    
                  f'{note_end[j]}'
                  f'{dict_[res]}')     # Табулированный вывод заметок по образцу


# Программа
print("Вот текущий список ваших заметок:")
output(note_list)
del_writerow = input(
    "Введите имя пользователя или заголовок "
    "для удаления заметки: "
)          # Ввод критерия для удаления заметки
question_ = input("Вы уверены, что хотите удалить заметку? (да/нет) ")
if question_ in [
    "д", "Д", "да", "Да", "Y", "y", "Yes", "yes"
]:          # Проверка на необходимость удаления введенной заметки
    delete_note(del_writerow)