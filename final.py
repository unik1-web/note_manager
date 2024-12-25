# Задание 5: Использование словаря
note0 = ("Имя пользователя: ","Содержание заметки: ","Статус заметки: ","Дата создания заметки в формате {10-11-2024}: ", "Дата истечения заметки (дедлайн) в формате {10-11-2024}: ","Заголовок: ")
note = ("username", "content", "status", "created_date", "issue_date", "titles")
note_dict = dict.fromkeys(note, "Ввод текста")
note_dict["titles"] = [1,2,3]
note_dict["username"] = input("Введите "+ note0[0])
note_dict["content"] = input("Введите "+ note0[1])
note_dict["status"] = input("Введите "+ note0[2])
note_dict["created_date"] = input("Введите "+ note0[3])
note_dict["issue_date"] = input("Введите "+ note0[4])
note_dict["titles"][0] = input("Введите "+ note0[5]+"1: ")
note_dict["titles"][1] = input("Введите "+ note0[5]+"2: ")
note_dict["titles"][2] = input("Введите "+ note0[5]+"3: ")
temp_created_date = note_dict["created_date"][: 5]
temp_issue_date = note_dict["issue_date"][: 5]
print()
print(note0[0],note_dict["username"])
print(note0[1],note_dict["content"])
print(note0[2],note_dict["status"])
print(note0[3][:21]+": ",temp_created_date)
print(note0[4][:21]+": ",temp_issue_date)
print(note0[5]+"1: ",note_dict["titles"][0])
print(note0[5]+"2: ",note_dict["titles"][1])
print(note0[5]+"3: ",note_dict["titles"][2])
