# Задание: Работа с несколькими заметками
from datetime import date

note_ = (
"имя пользователя: ", "заголовок заметки: ", "описание заметки: ", "статус заметки (новая, в процессе, выполнено):",
"дату создания заметки ", "дату истечения заметки (дедлайн) ")
status_ = ("новая", "в процессе", "выполнено")
fraza = {0: "Вы ввели текст без заглавной буквы, поэтому повторите ввод!",
         2: "Вы ввели несколько заголовков, поэтому повторите ввод заголовка заметки!",
         3: "Вы неправильно ввели статус заметки, повторите ввод!",
         4: "Неверный формат даты. Пожалуйста, убедитесь, что дата введена правильно."}
note = []
note_states = {}


def replace_dates(match_):  # Обработка любого ввода даты
    a = 0
    b = 0
    c = ['\\d{2}/\\d{2}/\\d{2,4}', '\\d{2}-\\d{2}-\\d{2,4}', '\\d{2}:\\d{2}:\\d{2,4}', '\\d{2}.\\d{2}.\\d{2,4}',
         '\\d{2,4}/\\d{2}/\\d{2}', '\\d{2,4}-\\d{2}-\\d{2}', '\\d{2,4}:\\d{2}:\\d{2}', '\\d{2,4}.\\d{2}.\\d{2}']
    d = ['%d/%m/%Y', '%d-%m-%Y', '%d:%m:%Y', '%d.%m.%Y', '%Y/%m/%d', '%Y-%m-%d', '%Y:%m:%d', '%Y.%m.%d']
    for i, j in zip(c, d):
        try:
            a = re.findall(i, match_)
            b = datetime.strptime(a[0], j)
            return b
        except:
            continue


def proverka(stroka_, ind_):
    counter = 0  # Счетчик заглавных букв
    if ind_ in [0, 1, 2]:
        for ch in stroka_:
            if ch.isupper(): counter += 1  # Проверка на заглавную букву
            if counter in [0] and ind_ in [0, 1, 2]:  # 0 заглавные буквы
                print(fraza[counter])
                note.pop(-1)
                return 0
    elif ind_ == 3 and stroka_ not in status_:
        print(fraza[3])
        return 0
    elif ind_ in [4, 5]:
        print(fraza[4])
        return 1
    # <class 'datetime.date'>


def vvod():
    c = -1
    lst = []
    while True:  # Ввод данных пользователем в элемент списка
        c += 1
        j = 0
        while True:  # Проверка на ввод данных в список
            # print(j,len(note))
            if j == 6: break
            note.append(input("Введите " + note_[j]))
            p = proverka(note[j], j)
            print(p)
            if p == 0:  # Проверка на ввод данных в список
                continue
            elif p == 1:
                note[j] = replace_dates(note[j])
                print("1", note[j])
                continue
            else:
                j += 1
        lst = note.copy()
        note_states[id(c)] = lst  # dict.fromkeys(objects, id(c)) #.update(id(c):)
        # print(note)
        # print(note_states)
        if input("Хотите добавить ещё одну заметку? (да/нет):  ") not in ["да", "Y", "y"]:
            break
        else:
            c += 1
            note.clear()


vvod()
print(note_states)

# # Пользователь вводит данные заметки (имя, заголовок, описание, статус, дату создания, дедлайн)
# note_dict["username"] = input("Введите "+ note0[0])
# note_dict["content"] = input("Введите "+ note0[1])
# note_dict["status"] = input("Введите "+ note0[2])
# # Сегодняшняя дата как дата создания заметки
# # current_date = date.today().strftime("%d-%m-%Y")
# # note_dict["created_date"] = current_date
# # print(note0[3][:21]+": ",note_dict["created_date"])
# note_dict["created_date"] = input("Введите "+ note0[3]+"в формате (день-месяц-год): ")
# note_dict["issue_date"] = input("Введите "+ note0[4]+"в формате (день-месяц-год): ")
# note_dict["titles"][0] = input("Введите "+ note0[5]+"1: ")
# note_dict["titles"][1] = input("Введите "+ note0[5]+"2: ")
# note_dict["titles"][2] = input("Введите "+ note0[5]+"3: ")
# # temp_created_date = note_dict["created_date"][: 5]
# # temp_issue_date = note_dict["issue_date"][: 5]

