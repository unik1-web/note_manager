# Этап3_Финальное_Юнин_Константин.
# Напишите функцию для создания новой заметки и возврата словаря.

import re
from datetime import date, datetime, timedelta

def create_note():
    note_ = ("имя пользователя: ",
             "заголовок заметки: ",
             "описание заметки: ",
             "статус заметки (новая, в процессе, выполнено. По умолчанию новая): ",
             "дату дедлайна (в любом формате или 7 дней от текущей даты по умолчанию):")        # Список элементов заметки для ввода
    status_ = ("новая", "в процессе", "выполнено")      # Список статусов заметки для ввода
    phrase = {0: "Вы ввели текст без заглавной буквы, поэтому повторите ввод!",
              3: "Вы неправильно ввели статус заметки, повторите ввод!",
              4: "Неверный формат даты. Пожалуйста, убедитесь, что дата введена правильно.",
              5: "Дата дедлайна не может быть раньше даты создания заметки, повторите ввод!"}        # Словарь фраз для вывода
    note_keys = ("username", "title", "content",
                   "status", "created_date", "issue_date")  # Список ключей словаря заметки
    note_states = {}    # Словарь заметки
    c = ['\\d{2}/\\d{2}/\\d{2,4}', '\\d{2}-\\d{2}-\\d{2,4}',
         '\\d{2}:\\d{2}:\\d{2,4}', '\\d{2}.\\d{2}.\\d{2,4}',
         '\\d{2,4}/\\d{2}/\\d{2}', '\\d{2,4}-\\d{2}-\\d{2}',
         '\\d{2,4}:\\d{2}:\\d{2}', '\\d{2,4}.\\d{2}.\\d{2}']  # Список шаблонов даты
    d = ['%d/%m/%Y', '%d-%m-%Y', '%d:%m:%Y',
         '%d.%m.%Y', '%Y/%m/%d', '%Y-%m-%d',
          '%Y:%m:%d', '%Y.%m.%d']  # Список форматов вывода даты
    note = []  # Список данных текущей заметки
    ind_ = 0  # Индекс заполнения списка для словаря заметок
    while ind_ < 5:  # Ввод данных пользователем
        string_ = input("Введите " + note_[ind_])  # Ввод данных пользователем
        if ind_ in [4]:        # Проверка даты дедлайна
            if string_ == "":       # Пустой ввод даты создания заметки сдвигает дидлайн на неделю
                string_ = str(date.today() + timedelta(weeks=1))
            a = [] # Список вхождений даты в строке
            b = 0  # Временная переменная преобразования даты
            for i, j in zip(c, d):  # Проверка ввода на наличие в строке даты
                try:
                    a = re.findall(i, string_)  # Поиск в строке ввода даты по имеющимся в списке [c] шаблонам
                    b = datetime.strptime(a[0], j)  # Преобразование вырезанной строки в тип datetime
                    b = datetime.date(b)  # Преобразование datetime в date
                    break   # Выход из цикла с аргументом b = date
                except:
                    continue    # Повторный ввод данных
            if b == 0:
                print(phrase[4])  # Вывод предупреждения об ошибке при неправильном вводе даты
                continue    # Повторный ввод данных
            if (b - date.today()).days <= 0:  # Дата создания меньше или равна даты дедлайна
                print(phrase[5])
                continue    # Повторный ввод данных
            note.append(str(date.today().strftime("%d.%m.%Y"))) # Присвоение словарю текущей даты в формате день.месяц.год
            note.append(str(b.strftime("%d.%m.%Y")))            # Присвоение словарю текущей даты в формате день.месяц.год
            break   # Выход из цикла
        elif ind_ in [3]:
            if string_ == "":   # Пустой ввод создания статуса заметки "новая"
                string_ = "новая"
            elif string_ not in status_:  # Проверка на вхождение ввода в список статусов заметки
                print(phrase[3])
                continue    # Повторный ввод данных
        elif ind_ in [0, 1, 2]:  # Проверка на ввод имени заметки, заголовка и описания
            if string_ == "":
                print(phrase[0])
                continue
            counter = 0  # Счетчик заглавных букв
            error = 0    # Счетчик ошибок
            for ch in string_:
                if ch.isupper():
                    counter += 1    # Проверка на заглавную букву
                if counter in [0]:  # 0 заглавных букв - ошибка
                    print(phrase[0])
                    error = 1
                    break  # Выход из цикла с аргументом error = 1, т.е. нужен повторный ввод
            if error == 1:
                continue  # Повторный ввод данных
        note.append(string_)
        ind_ += 1
    for i, j in zip(note_keys,range(6)):
        note_states[i] = note[j]        # Внесение данных в словарь
    print("Заметка создана:", note_states)

# Программа "Менеджер заметок"
create_note()
