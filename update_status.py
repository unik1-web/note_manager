# Проверка и обновление статуса заметки

def vvod(stroka_):
    s = stroka.lower()                               # Приведение статуса к нижнему регистру
    print(s)
    if not s.isdigit() and s in status_:        # Проверка на ввод нового статуса в текстовом формате
        s = str(status_.index(s)+1)             # Изменение переменной текущего статуса заметки в зависимости от
    else:
        s = "1"
    return                           # Выход из цикла while

# Инициализация списка  вспомогательных переменных
note_ = {"status":"в процессе"}                     # Словарь состояния статуса заметки
status_=("выполнено", "в процессе", "отложено")     # Кортеж статусов заметки
s = "2"                                             # Переменная текущего статуса заметки
print('Текущий статус заметки: "{}"'.format(note_["status"]))
print("Выберите новый статус заметки: 1. выполнено, 2. в процессе, 3. отложено")
while True:
    try:                                            # Проверка ввода на корректность
        # s = input("Ваш выбор: ")                    # Ввод статуса пользователем
        s = vvod(input("Ваш выбор: "))
        note_["status"] = status_[int(s)-1]         # Присваиваем словарю значение из кортежа статусов заметки
        print('Статус заметки успешно обновлён на: "{}"'.format(note_["status"]))
        break
    except:
        print(f"Неверный ввод статуса заметки: {s}")                # Вывод сообщения об ошибке при неправильном вводе