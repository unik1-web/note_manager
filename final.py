import username
note0 = ("Имя пользователя: ","Содержание заметки: ","Статус заметки: ","Дата создания заметки в формате {10-11-2024}: ", "Дата истечения заметки (дедлайн) в формате {10-11-2024}: ",["Заголовок 1: ","Заголовок 2: ","Заголовок 3: "])
note = [*note0]
note[0] = input(note[0])
note[1] = input(note0[1])
note[2] = input(note0[2])
note[3] = input(note0[3])
note[4] = input(note0[4])
note[5][0] = input(note0[5][0])
note[5][1] = input(note0[5][1])
note[5][2] = input(note0[5][2])
temp_created_date = note[3][0: 5]
temp_issue_date = note[4][0: 5]
print(note)
print(note0[0], note[0])
print(note0[1], note[1])
print(note0[2], note[2])
print(note0[3][:21]+": ", temp_created_date)
print(note0[4][:21]+": ", temp_issue_date)
print("Заголовки:", note[5])
