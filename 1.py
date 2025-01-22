# file = open("example.txt", 'w', encoding='utf-8' )
# print(file.writable())
# # file.write("Инфо один\n")
# # file.write("Info Two\n")
# # file.write("Инфо три\n")
# file.writelines(["Инфо один\n", "Info Two\n", "Инфо один\n"])
# # file.close()
# counter = 1
# # info = input("Введите информацию: \n")
#
# while info:
#     file.write(f"{counter}.{info}\n")
#     counter += 1
#     info = input()
#
# file.close()
# print(file.read(5))
# print(file.readlines(23))
# print(file.readline())

# info = file.read()
# info = info.replace('\n', ' ') #метод замены \n на пробел
# symbols = (',','.',' -',':')
# for sym in symbols:
#     info = info.replace(sym, '')
# result = info.split()
# print(result)
# print(len(result))
# file.close()
# def test_(*params):
#     print(type(params))
#     print(params)
#
# test_(1,2,3,4)
# def summator(txt,*values):
#     s=0
#     for i in values:
#         s+=i
#     return f'{txt}{s}'
#
# print(summator('Summa = ',1,2,3,4,5))
# from itertools import zip
# note = [
#     1,2,3
# ]
# not_ = {
#     "John": 90,
#     "Sarah": 85,
#     "Emma": 93}
# notes = [
#     {
#     "John": 90,
#     "Sarah": 85,
#     "Emma": 93},
#     {
#     "John": 90,
#     "Sarah": 85,
#     "Emma": 93
#     },
#     {
#     "John": 90,
#     "Sarah": 85,
#     "Emma": 93
#     }
# ]
# key_=[]
# values_=[]
# # print(notes)
# for i, dikt_ in enumerate(notes):
#     for key, values in dikt_.items():
#         # dikt_[j] = dikt_.pop(k)
#         key_.append(key)
#         values_.append(values)
# print(key_, values_)
# d = dict(zip(note, values_))
# print(d)
# print(notes)
import os.path
path = 'C:/Users/adml/Documents/GitHub/note_manager1/file.txt'
print(os.path.exists(path))
try:
    with open('python.exe', encoding='UTF-8') as file:
        print(file.read())
except FileNotFoundError:
    print("Что-то случилось")
except UnicodeDecodeError:
    print("Что-то случилось 2")
# with open('python.exe', encoding='UTF-8') as file:
#     print(file.read())
