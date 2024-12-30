from datetime import date, datetime

# Получение текущей даты
current_date = date.today()
print("Текущая дата: ", current_date)  # Вывод в формате YYYY-MM-DD 
while True:
    try:
        # код, который может вызвать исключение (Проверка введенной даты на корректность)
        # Ввод даты пользователем
        issue_date = input("\nВведите дату дедлайна (в формате день-месяц-год): ")
        # Правильное преобразование строки в объект datetime
        issue_date = datetime.strptime(issue_date,format("%d-%m-%Y"))
        issue_date = datetime.date(issue_date)
        num_days = (issue_date - current_date).days
        if issue_date < current_date:
            print('\nВнимание! Дедлайн истёк {} дня назад.'.format(-num_days))
        elif issue_date > current_date:
            print('\nДо дедлайна осталось {} дня.'.format(num_days))
        else:
            print('\nДедлайн сегодня!')
        break
    except ValueError:
        # код для обработки исключения, которое может возникнуть в блоке try
        print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")