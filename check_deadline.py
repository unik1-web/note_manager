# Обработка дедлайнов
from datetime import date, datetime

# Функции
def today():                           # Получение текущей даты
    return date.today()


def delta(issue):                      # Разница в днях между датами
    return (today() - issue).days


def day_(num_, fraza1_, fraza2_):      #Вывод предупреждения с разным склонением слова "день"
    if num_ in [
            1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121, 131, 141, 151, 161,
            171, 181, 191
    ]:  
        print('{} {} день {}.'.format(fraza1_, num_, fraza2_))
    elif num_ in [
            2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63,
            64, 72, 73, 74, 82, 83, 84, 92, 93, 94, 102, 103, 104, 122, 123,
            124
    ]: 
        print('{} {} дня {}.'.format(fraza1_, num_, fraza2_))
    else:  
        print('{} {} дней {}.'.format(fraza1_, num_, fraza2_))


def vvod(issue_):
    # if len(issue_) == 0: return 0
    current_ = today()                # Получение текущей даты
    issue_ = datetime.strptime(
        issue_, format("%d-%m-%Y"))   # Преобразование ввода в объект datetime
    issue_ = datetime.date(issue_)    # Преобразование ввода в объект date
    num_days = delta(issue_)          # Разница в днях между датами
    if issue_ < current_:
        day_(num_days, "Внимание! Дедлайн истёк ", "назад"
             )                        # Вывод предупреждения при положительной разницы дней       
    elif issue_ > current_:
        day_(-num_days, "До дедлайна осталось ",""
             )                        # Вывод предупреждения при отрицательной разнице дней       
    else:
        print('Дедлайн сегодня!')
    return 0                          # Выход из цикла while


# Программа
current_date = today()                # Получение текущей даты
print("Текущая дата: ",
      today().strftime("%d.%m.%Y"))   # Вывод в формате DD-MM-YYYY
while True:                           # Ввод даты дедлайна
    try:  # код, который может вызвать исключение (Проверка введенной даты на корректность)
        issue_date = input("Введите дату дедлайна (в формате день-месяц-год): "
                           )          # Ввод даты пользователем
        if vvod(issue_date) == 0: break      # Выход из цикла while
    except:                           # Любая ошибка при вводе даты пользователем
        print(
            "Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год."
        )
