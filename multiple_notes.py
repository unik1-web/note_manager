# Задание: Работа с несколькими заметками
from datetime import date

note0 = ("имя пользователя: ","заголовок заметки: ","описание заметки: ","статус заметки (новая, в процессе, выполнено):","дата создания заметки ", "дату истечения заметки (дедлайн) ")
note = ("username", "content", "status", "created_date", "issue_date", "titles")
note_dict: dict[str, str] = dict.fromkeys(note, "Ввод текста")
# note_dict["titles"] = [1,2,3]
# Пользователь вводит данные заметки (имя, заголовок, описание, статус, дату создания, дедлайн)
note_dict["username"] = input("Введите "+ note0[0])
note_dict["content"] = input("Введите "+ note0[1])
note_dict["status"] = input("Введите "+ note0[2])
# Сегодняшняя дата как дата создания заметки
# current_date = date.today().strftime("%d-%m-%Y")
# note_dict["created_date"] = current_date
# print(note0[3][:21]+": ",note_dict["created_date"])
note_dict["created_date"] = input("Введите "+ note0[3]+"в формате (день-месяц-год): ")
note_dict["issue_date"] = input("Введите "+ note0[4]+"в формате (день-месяц-год): ")
note_dict["titles"][0] = input("Введите "+ note0[5]+"1: ")
note_dict["titles"][1] = input("Введите "+ note0[5]+"2: ")
note_dict["titles"][2] = input("Введите "+ note0[5]+"3: ")
# temp_created_date = note_dict["created_date"][: 5]
# temp_issue_date = note_dict["issue_date"][: 5]
print()
print(note0[0],note_dict["username"])
print(note0[1],note_dict["content"])
print(note0[2],note_dict["status"])
print(note0[3][:21]+": ",note_dict["created_date"])
print(note0[4][:22]+": ",note_dict["issue_date"])
print(note0[5]+"1: ",note_dict["titles"][0])
print(note0[5]+"2: ",note_dict["titles"][1])
print(note0[5]+"3: ",note_dict["titles"][2])
