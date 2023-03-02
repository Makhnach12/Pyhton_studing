import json

salaries = []
persons = []


def salary_counter(salary, name, pos):
    if name + pos + str(salary) not in persons:
        salaries.append(salary)
        persons.append(name + pos + str(salary))


def information_taker(text):
    if type(text) is not list:
        salary_counter(text['salary'], text['name'], text['position'])
        if len(text['subordinates']) != 0:
            information_taker(text['subordinates'])
    else:
        for i in text:
            information_taker(i)


with open('zad2.json', 'r') as f:
    text = json.load(f)

information_taker(text)
print('Средняя зарплата:', sum(salaries) / len(salaries))
salaries.sort()
if len(salaries) % 2 == 1:
    print('Медианная зарплата:', salaries[len(salaries) // 2])
else:
    print('Медианная зарплата:', (salaries[len(salaries) // 2] + salaries[len(salaries) // 2 - 1]) / 2)
