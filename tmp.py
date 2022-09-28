with open ('db.csv', 'r') as reading:
    data = reading.read()
lst = data.split('\n')
sorted_list = sorted(lst, reverse = False)
print (sorted_list)
for num in range(len(sorted_list)):
    if sorted_list[num] == 'name;position;salary;address;age;phone':
        count1 = 0
        count2 = 1
        while count1 < num:
            sorted_list[num - count1] = sorted_list[num - count2]
            count1 += 1
            count2 += 1
sorted_list[0] = 'name;position;salary;address;age;phone'
print (sorted_list)
# for item in lst:
#     item = item.split(';')
#     for salary_data in range(2,3):
#         if item[salary_data].isdigit():
#             list_of_salary.append(int(item[salary_data]))
# print(f'такие вот зарплаты {list_of_salary}')
# print(f'минимальная зарплата {min(list_of_salary)}')
# print(f'максимальная зарплата {max(list_of_salary)}')
# print(f'выплачивается в месяц всего {sum(list_of_salary)}')
# print(f'средняя зарплата {statistics.mean(list_of_salary)}')
