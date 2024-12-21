username = input("Имя пользователя: ")
title1 = input("Заголовок 1: ")
title2 = input("Заголовок 2: ")
title3 = input("Заголовок 3: ")
title = [title1, title2, title3]
content = input("Заметка: ")
status = input("Статус заметки: ")
created_date = input("Дата создания заметки в формате {10-11-2024}: ")
issue_date = input("Дата истечения заметки (дедлайн) в формате {10-11-2024}: ")
temp_created_date = created_date[0: 5]
temp_issue_date = issue_date[0: 5]
print()
print("Имя пользователя:", username)
print("Заголовок:", title)
print("Заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки (дедлайн):", temp_issue_date)
