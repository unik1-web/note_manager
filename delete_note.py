# Grade 1. Этап 2: Задание 5: Удаление заметок
note_states = {1:["Алексей", "Список покупок", "Купить продукты на неделю"],
               2:["Мария", "Учеба", "Подготовиться к экзамену"]}
note_end = ("Имя: ", "Заголовок: ", "Описание: ","Статус: ","Дата создания: ", "Дедлайн: ")

def delete_note(del_):
    k, l = 0, 0
    for k in range(len(note_states.keys())):
        for l in range(3):
            if del_ == note_states[k + 1][l]:  # Проверка на необходимость удаления введенной заметки
                del note_states[k + 1]         # Удаление заметки с искомым критерием
                print("Успешно удалено. Остались следующие заметки:")
                vivod(note_states)             # Вывод оставшихся заметок
                return
    print("Заметок с таким именем пользователя или заголовка не найдено.")
    return

def  vivod(note_id):
    i , j = 0, 0
    for i in note_id.keys():                   # Вывод заметок
        print(i , ". ", end='')                # Вывод номера заметки
        for j in range(3):                     # Вывод данных заметки с форматом табулирования строк
            if j in [0]:
                print("\t", note_end[j], note_id[i][j])
            else:
                print("\t\t", note_end[j], note_id[i][j])

# Программа
print("Текущие заметки:")
vivod(note_states)
del_kriteriy = input("Введите имя пользователя или заголовок для удаления заметки: ")
delete_note(del_kriteriy)
