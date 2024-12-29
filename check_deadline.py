import datetime
from datetime import date, datetime, timedelta

# Получение текущей даты
current_date = date.today()
print("Текущая дата: ", current_date)  # Вывод в формате YYYY-MM-DD 
# Ввод даты пользователем
# issue_date =input("\nВведите дату дедлайна (в формате день-месяц-год): ")
# Проверка введенной даты на корректность
while True:
    issue_date =input("\nВведите дату дедлайна (в формате день-месяц-год): ")
    for s in issue_date:
        if s.isdigit() and int(s) in [1,2,3,4,5,6,7,8,9,0]:    # Условие ввода цифры от 1 до 3
            break                                # Если условие выполнено, то выходим из цикла
    break
if len(issue_date) != 10 or issue_date[2] != '-' or issue_date[5] != '-' or issue_date[:1].isalpha() :
    print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")
    issue_date =input("\nВведите дату дедлайна (в формате день-месяц-год): ")
# Правильное преобразование строки в объект datetime
issue_date = datetime.strptime(issue_date, "%d-%m-%Y") 
issue_date = datetime.date(issue_date)
num_days = (issue_date - current_date).days
print('\nВнимание! Дедлайн истёк {} дня назад.'.format(-num_days)) if issue_date < current_date else print('\nДо дедлайна осталось {} дня.'.format(num_days))
