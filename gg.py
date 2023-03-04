import json

salaries = []
persons = []


def process_salary(salary, name, pos):
    if name + pos + str(salary) not in persons:
        salaries.append(salary)
        persons.append(name + pos + str(salary))


def process_information(employee_list):
    if type(employee_list) is not list:
        process_salary(employee_list['salary'], employee_list['name'], employee_list['position'])
        if len(employee_list['subordinates']) != 0:
            process_information(employee_list['subordinates'])
    else:
        for employee in employee_list:
            process_information(employee)


with open('zad2.json', 'r') as f:
    text = json.load(f)

process_information(text)
print('Средняя зарплата:', sum(salaries) / len(salaries))
salaries.sort()
if len(salaries) % 2 == 1:
    print('Медианная зарплата:', salaries[len(salaries) // 2])
else:
    print('Медианная зарплата:', (salaries[len(salaries) // 2] + salaries[len(salaries) // 2 - 1]) / 2)
