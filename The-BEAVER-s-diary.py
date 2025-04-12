import sqlite3

connection = sqlite3.connect('diary.db')

cursor = connection.cursor()

sql = '''
    create table if not exists progress
    (
        id integer primary key autoincrement,
        subject text,
        grade integer
    );
'''

cursor.execute(sql)
connection.commit()

print("ПРИВЕТ ОТ БОБРА")
print("Что прикажете делать повелитель?")

while True:
    action = input("Бобер> ")
    if action == 'exit':
        break

    if action == 'help':
        print("help - список команд")
        print("show - показать список оценок")
        print("add [код предмета] [оценка] - добавить запись")
        print(" Коды предметов")
        print("     m-Математика")
        print("     g-Геометрия")
        print("     i-Информатика")
        print("update [id] [новая оценка] - обновить оценку")
        print("del [id] - удалить запись")
        print("exit - выход")

    elif action == 'show':
        cursor.execute('select * from progress')
        result = cursor.fetchall()

        if len(result) == 0:
            print("Данные не заданы")
        else:
            for element in result:
                print("id = {} {} - {}".format(element[0], element[1], element[2]))


    elif action[:3] == 'add':
        subject_code = action[4]

        subject = None

        if subject_code == 'm':
            subject = 'Математика'
        elif subject_code == 'g':
            subject = 'Геометрия'
        elif subject_code == 'i':
            subject = 'Информатика'
        else:
            print("Не удалось определить предмет")
            continue

        grade = action[6]

        cursor.execute(
            'insert into progress(subject, grade) values("{}", {})'.format(subject, grade)
        )
        connection.commit()

        print('ok')

    elif action[:6] == 'update':
        id_u = action[7]
        new_grade = action[9]

        cursor.execute(
            'update progress set grade = {} where id = {};'.format(new_grade, id_u)
        )
        connection.commit()
        print('ok')

    elif action[:3] == 'del':
        id_u = action[4]
        cursor.execute(
            'delete from progress where id = {};'.format(id_u)
        )
        connection.commit()
        print('ok')

    else:
        print("Команда не поддерживается")

connection.close()
print("ДО ВСТРЕЧИ, ХОЗЯИН!")