import username

note=["Имя пользователя: ","Содержание заметки: ","Статус: ","Дата создания заметки в формате {10-11-2024}: ", "Дата истечения заметки (дедлайн) в формате {10-11-2024}: ",["Заголовок 1","Заголовок 2","Заголовок 3"]]
note[0] = input(note[0])
note[1] = input(note[1])
note[2] = input(note[2])
note[3] = input(note[3])
note[4] = input(note[4])
note[5] [1] = input(note[5][1])
note[5][2] = input(note[5][2])
note[5][3] = input(note[5][3])
temp_created_date = note[3][0: 5]
temp_issue_date = note[4][0: 5]
print(note)
print("Имя пользователя:", note[0])
print("Содержание заметки:", note[1])
print("Статус заметки:", note[2])
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки (дедлайн):", temp_issue_date)
print("Заголовки:", note[5])
