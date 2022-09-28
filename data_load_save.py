def find_info():
    print('модуль поиска')
    user_inp = input('введите данные для поиска: ').lower()
    with open ('db.csv', 'r') as reading:
        marks = ['имя -', 'должность -', 'зарплата -', 'адрес -', 'возраст -', 'телефон -']
        for line in reading:
            if line.lower().count(user_inp):
                print (f'данные найдены:')
                output_info = zip (marks, line.split(";"))
                for item in output_info:
                    for inside_item in item:
                        print (inside_item, end =' ')
                    print('')

def add_info():
    print ('модуль добавления')
    user_inp = input('введите имя, должность, зарплата, адрес, возраст, телефон (через ;) - ')
    with open ('db.csv', 'a') as adding:
        adding.writelines(user_inp)
    print (f'данные добавлены {user_inp}')
    sortirovka

def delete_info():
    print ('модуль удаления')
    user_inp = input('введите данные для удаления: ').lower()
    with open ('db.csv', 'r') as reading:
        for line in reading:
            if line.lower().count(user_inp):
                print (f'эти данные будут удалены {line} ')
                delete_line(line)
    sortirovka
                
def delete_line(line):
    with open ('db.csv', 'r') as reading:
        data = reading.read()
        data = data.replace(line, '')
    with open('db.csv', 'w') as writing_operation:
        writing_operation.writelines(data)

def import_info():
    print ('модуль импортирования')
    user_inp = input('введите название файла для импорта: ')
    with open (user_inp, 'r') as reading:
        data = reading.read()
    with open ('db.csv', 'a') as adding:
        adding.writelines('\n')
        adding.writelines(data)
    print (f'данные добавлены \n{data}')
    sortirovka ()

def export_info():
    print ('модуль экспортирования')
    user_inp = input('введите название файла для экспора: ')
    with open ('db.csv', 'r') as reading:
        data = reading.read()
    with open(user_inp, 'w') as writing_operation:
        writing_operation.writelines(data)
    print (f'данные экспортированы \n{data}')

def change_info():
    print ('модуль корректировки')
    user_inp = input('введите данные для корректировки: ').lower()
    with open ('db.csv', 'r') as reading:
        list_of_correction = []
        for line in reading:
            if line.lower().count(user_inp):
                print (f'эти данные будут скорректированы {line} ')
                list_of_correction.append(line)
        print (f'будет скорректировано {list_of_correction}')
    with open ('db.csv', 'r') as reading:
        data = reading.read()
        new_info = remake_line(list_of_correction)
        data = data.replace(list_of_correction[0], new_info + '\n')
    with open('db.csv', 'w') as writing_operation:
        writing_operation.writelines(data)
    marks = ['имя -', 'должность -', 'зарплата -', 'адрес -', 'возраст -', 'телефон -']
    output_info = zip (marks, new_info.split(";"))
    print ('добавлены новые данные: ')
    for item in output_info:
        for inside_item in item:
            print (inside_item, end =' ')
        print('')
    sortirovka()

def remake_line(list_of_correction):
    print (f'модуль корректировки строки\n {list_of_correction}')
    new_line = input('введите имя, должность, зарплата, адрес, возраст, телефон (через ;) - ')
    return new_line

import statistics
def salary_info():   
    with open ('db.csv', 'r') as reading:
        data = reading.read()
    lst = data.split('\n')
    list_of_salary = []
    for item in lst:
        item = item.split(';')
        for salary_data in range(2,3):
            if item[salary_data].isdigit():
                list_of_salary.append(int(item[salary_data]))
    print(f'такие вот зарплаты {list_of_salary}')
    print(f'минимальная зарплата {min(list_of_salary)}')
    print(f'максимальная зарплата {max(list_of_salary)}')
    print(f'выплачивается в месяц всего {sum(list_of_salary)}')
    print(f'средняя зарплата {statistics.mean(list_of_salary)}')

def age_info(): 
    with open ('db.csv', 'r') as reading:
        data = reading.read()
    lst = data.split('\n')
    list_of_age = []
    for item in lst:
        item = item.split(';')
        for age_data in range(4,5):
            if item[age_data].isdigit():
                list_of_age.append(int(item[age_data]))
    print(f'такие вот возрасты {list_of_age}')
    print(f'минимальный возраст {min(list_of_age)}')
    print(f'максимальный возраст {max(list_of_age)}')
    print(f'средний возраст {statistics.mean(list_of_age)}')

def sortirovka():
    print('идет сортировка')
    with open ('db.csv', 'r') as reading:
        data = reading.read()
    lst = data.split('\n')
    sorted_list = sorted(lst, reverse = False)
    for num in range(len(sorted_list)):
        if sorted_list[num] == 'name;position;salary;address;age;phone':
            count1 = 0
            count2 = 1
            while count1 < num:
                sorted_list[num - count1] = sorted_list[num - count2]
                count1 += 1
                count2 += 1
    sorted_list[0] = 'name;position;salary;address;age;phone'
    for item in range (0,len(sorted_list) * 2 - 1,2):
        sorted_list.insert(item, '\n')
    
    with open('db.csv', 'w') as writing_operation:
        writing_operation.writelines(sorted_list)