salaries = []
persons = []


def salary_counter(salary, name, pos):
    if name + pos + salary not in persons:
        salaries.append(float(salary[0:len(salary) - 1]))
        persons.append(name + pos + salary)


f = open('input2.txt', 'r')
name = ''
pos = ''
for line in f:
    answer = line.split()
    if answer[0] == 'salary:':
        salary_counter(answer[1], name, pos)
    elif answer[0] == 'name:':
        name = answer[1]
    elif answer[0] == 'position:':
        pos = answer[1]
print('Средняя зарплата:', sum(salaries) / len(salaries))
salaries.sort()
if len(salaries) % 2 == 1:
    print('Медианная зарплата:', salaries[len(salaries) // 2])
else:
    print('Медианная зарплата:', (salaries[len(salaries) // 2] + salaries[len(salaries) // 2 - 1]) / 2)
