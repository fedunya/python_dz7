def user_input(msg_out, n):
    a = ['1','2','3','4']
    num = input(msg_out)
    while num not in a[:n]: num = input('Неверный ввод! Повторите: ')
    return int(num)
def begin():
    print('МЕНЮ:\n1. Импорт контактов из файла.\n2. Экспорт контактов в файл.\n'
        '3. Просмотр телефонной книги на экране.\n4. Выход из программы.')
    key = user_input('Введите номер выбранного пункта меню: ', 4)
    if key == 1:
        num = user_input('Выберите формат импортируемых данных:\n1. .txt\n2. .json\n-> ', 2)
        if num == 1: imp.data_to_csv('phonebook.csv', imp.import_txt('phonebook.txt'))
        else: imp.data_to_csv('phonebook.csv', imp.import_json('phonebook.json'))
        print('Контакты успешно импортированы в телефонную книгу.')
        begin()
    elif key == 2:
        num = user_input('Выберите формат экспорта контактов из телефонной книги:\n'
                        '1. .txt\n2. .json\n-> ', 2)
        data, fields, count = ex.csv_to_data('phonebook.csv')
        if num == 1: ex.export_txt('phonebook.txt', data, fields, count)
        else: ex.export_json('phonebook.json', data, fields, count)
        print('Контакты успешно экспортированы из телефонной книги.')
        begin()
    elif key == 3:
        num = user_input('Выберите формат вывода телефонной книги на экран:\n'
                        '1. Горизонтальный - в одной строке один контакт.\n'
                        '2. Вертикальный - элементы контакта выводятся вертикально,'
                        ' разделитель - пустая строка.\n-> ', 2)
        data, fields, count = ex.csv_to_data('phonebook.csv')
        if num == 1:            
            vp.view_horizontal(data, fields, count)
            a = input('Нажмите любую кнопку для продолжения')
        else:            
            vp.view_vertical(data, fields, count)
            a = input('Нажмите любую кнопку для продолжения')
        begin()
    else: print('Вы завершили работу программы. До свидания!')
    return

import import_from_file as imp
import export_in_file as ex
import view_phonebook as vp
