# Этап3_Финальное_Юнин_Константин.
# Задание 3: Функция отображения заметок
import re
from datetime import date, datetime


note_states = {'username': 'Алексей', 
               'title': 'Список покупок', 
               'content': 'Купить продукты на неделю', 
               'status': 'новая', 
               'created_date': '10.01.2025', 
               'issue_date': '17.01.2025'}    # Список словарей заметки
note = ['username', 'title', 'content', 
        'status', 'created_date', 'issue_date']
status_ = ("новая", "в процессе", "выполнено")  # Список статусов заметки для ввода
note_end = ("Имя: ", "Заголовок: ",
            "Описание: ","Статус: ",
            "Дата создания: ", "Дедлайн: ")                               # Список элементов заметки для вывода
vivod_tab = ("\t", "\t\t", "\t\t", "\t\t",
             "\t\t", "\t\t")                              # Список табуляции элементов заметки для вывода


def display_notes(notes):
    for i in note_states.keys():                # Вывод заметок
        print(i , ". ", end='')                 # Вывод номера заметки
        for j in range(3):                      # Вывод данных с форматом табулирования строк из списка vivod_tab
            print(
                f'{vivod_tab[j]}{note_end[j]}'
                f'{note_states[i][j]}'
                  )

# Программа
print("Вот текущий список ваших заметок:")
display_notes(ote_states)