# Задание: Работа с несколькими заметками
import re
from datetime import date, datetime

note_ = ("имя пользователя: ", "заголовок заметки: ", "описание заметки: ",
         "статус заметки (новая, в процессе, выполнено): ",
         "дату создания заметки: ", "дату истечения заметки (дедлайн): ")
note_end = ("Имя: ", "Заголовок: ", "Описание: ","Статус: ","Дата создания: ", "Дедлайн: ")
status_ = ("новая", "в процессе", "выполнено")
fraza = {0: "Вы ввели текст без заглавной буквы, поэтому повторите ввод!",
         1: "Вы ввели заголовок, который уже вводили ранее, поэтому повторите ввод заголовка заметки!",
         2: "Вы ввели несколько заголовков, поэтому повторите ввод заголовка заметки!",
         3: "Вы неправильно ввели статус заметки, повторите ввод!",
         4: "Неверный формат даты. Пожалуйста, убедитесь, что дата введена правильно.",
         5: "Дата дедлайна раньше даты создания заметки, повторите ввод!"}
ID = []                                         # Ключ ID для уникальности каждой заметки
note = []                                       # Список данных текущей заметки
note_states = {}                                # Список словарей заметки


def replace_dates(match_):                      # Обработка любого ввода даты
    a = []
    b = 0
    c = ['\\d{2}/\\d{2}/\\d{2,4}', '\\d{2}-\\d{2}-\\d{2,4}', '\\d{2}:\\d{2}:\\d{2,4}', '\\d{2}.\\d{2}.\\d{2,4}',
         '\\d{2,4}/\\d{2}/\\d{2}', '\\d{2,4}-\\d{2}-\\d{2}', '\\d{2,4}:\\d{2}:\\d{2}', '\\d{2,4}.\\d{2}.\\d{2}']
    d = ['%d/%m/%Y', '%d-%m-%Y', '%d:%m:%Y', '%d.%m.%Y', '%Y/%m/%d', '%Y-%m-%d', '%Y:%m:%d', '%Y.%m.%d']
    for i, j in zip(c, d):                      # Проверка ввода на наличие в строке даты
        try:
            a = re.findall(i, match_)           # Поиск в строке ввода даты по имеющимся в списке [c] шаблонам
            b = datetime.strptime(a[0], j)      # Преобразование вырезанной строки в тип datetime
            b = datetime.date(b)                # Преобразование datetime в date
            return b                            # Выход из функции с аргументом date
        except:
            continue
    print(fraza[4])
    return 0                                    # Выход из функции с аргументом 0, т.е. нужен повторный ввод даты

def proverka(stroka_, ind_):
    counter = 0                                 # Счетчик заглавных букв
    if ind_ in [4] and stroka_ == "":           # Пустой ввод даты создания заметки
        note[ind_] = date.today()               # Присвоение дате создания заметки текущей даты
        return
    elif ind_ in [4, 5]:
        note[ind_] = replace_dates(note[ind_])  # Проверка на ввод даты и преобразование в тип datetime
        if note[ind_] == 0: return 0            # Данные не прошли проверку. Выход из функции с аргументом 0
        if ind_ in [5] and (note[ind_]-note[ind_-1]).days <= 0: # Дата создания меньше или равна даты дедлайна
            print(fraza[5])
            return 0                            # Выход из функции с аргументом 0, т.е. нужен повторный ввод
    elif ind_ == 3 and stroka_ not in status_:  # Проверка на вхождение ввода в список статусов заметки
        print(fraza[3])
        return 0                                # Выход из функции с аргументом 0, т.е. нужен повторный ввод статуса
    elif ind_ in [0, 1, 2]:                     # Проверка на ввод имени заметки, заголовка и описания
        for ch in stroka_:
            if ch.isupper(): counter += 1               # Проверка на заглавную букву
            if counter in [0] and ind_ in [0, 1, 2]:    # 0 заглавных букв - ошибка
                print(fraza[0])
                return 0                        # Выход из функции с аргументом 0, т.е. нужен повторный ввод
        for i in range(e-1):
            if stroka_ == note_states[ID[i]][1]:# Проверка заголовка заметки на уникальность
                print(fraza[1])
                return 0                        # Выход из функции с аргументом 0, т.е. нужен повторный ввод

def vvod():
    global e
    e = -1                                      # Индекс заметок пользователя
    lst = []                                    # Копия списка ввода
    while True:                                 # Ввод данных пользователем
        e += 1
        j = 0                                   # Индекс заполнения списка для словаря заметок
        while True:
            if j == 6: break                    # Выход при заполнении списка словаря заметок
            if j in [0,1,2]:                    # Ввод данных пользователем
                note.append(input("Введите " + note_[j]))
            elif j in [4]:
                note.append(input("Введите дату создания заметки или нажмите Enter для ввода текущей даты: "))
            else:
                note.append(input("Введите " + note_[j]))
            if proverka(note[j], j) == 0:       # Введенные данные не прошли проверку
                note.pop(-1)                    # Удаление из списка неправильно введенной строки
                continue
            j += 1
        lst = note.copy()                       # Копия списка ввода
        ID.append(id(e))                        # Создание ключа ID
        note_states[ID[-1]] = lst               # Внесение данных в словарь с ключем ID
        if input("Хотите удалить эту заметку? (да/нет):  ") in ["да", "Y", "y"]:
            del note_states[ID[-1]]             # Проверка на необходимость удаления введенной заметки
            del ID[-1]
            e -= 1
        if input("Хотите добавить ещё одну заметку? (да/нет):  ") not in ["да", "Y", "y"]:
            break                               # Проверка на необходимость ввода еще одной заметки
        else:
            e += 1
            note.clear()                        # Очистка списка ввода данных
print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
print("Вводите имя, заголовок и описание заметки с заглавной буквы, а даты в любом числовом формате (10-10-2024 или подобном):")
vvod()
print("Список заметок:")
for i in range(len(ID)):                        # Вывод списка заметок с форматом табулирования строк
    print(i+1,". ", end='')                     # Вывод номера заметки
    for j in range(6):                          # Вывод данных заметки
        if j in [0]:
            print("\t",note_end[j], note_states[ID[i]][j])
        else:
            print("\t\t",note_end[j], note_states[ID[i]][j])