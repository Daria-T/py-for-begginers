# (name, family_name, age, street, building, apartment, experience, salary)
friends = {
    ('Лена', 'Иванова', 17, 'Пушкина', 10, 3): ('Лена', 'Иванова', 17, 'Пушкина', 10, 3, 5, 2300),
    ('Оксана', 'Иванова', 20, 'Пушкина', 10, 3): ('Оксана', 'Иванова', 20, 'Пушкина', 10, 3, 7, 5500),
    ('Петя', 'Петров', 35, 'Юрша', 25, 1): ('Петя', 'Петров', 35, 'Юрша', 25, 1, 10, 6500),
    ('Алексей', 'Устинов', 17, 'Уинская', 4, 34): ('Алексей', 'Устинов', 17, 'Уинская', 4, 34, 2, 10500)
}


def find_person(persons, filed):
    target = None
    field_index = -1
    if 'age' == filed:
        field_index = 2
    if 'experience' == filed:
        field_index = 6
    if 'salary' == filed:
        field_index = 7

    if field_index > 0:
        max_value = 0
        for key, person in persons.items():
            if max_value <= person[field_index]:
                max_value = person[field_index]

        for key, person in persons.items():
            if person[field_index] == max_value:
                target = person

    return target


print('Выбираем самого: взрослого (age), опытного (experience), богатого (salary).')
sort_filed = input('Введите поле для поиска самого-самого:')
result = find_person(friends, sort_filed)
if result:
    print(result)
else:
    print('Сортировка по полю: ' + sort_filed + ' не поддерживается')
