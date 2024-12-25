#Задание 2: Изменение формата вывода даты
username = "Ivan"
title = "Заголовок"
content = "Заметка"
status = "Статус заметки"
created_date = "10-11-2024"
issue_date = "10-12-2024"
temp_issue_date = created_date[: 5]
temp_created_date = issue_date[: 5]
print("Имя пользователя: ", username)
print("Заголовок: ", title)
print("Заметка: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", temp_created_date)
print("Дата истечения заметки (дедлайн): ", temp_issue_date)
