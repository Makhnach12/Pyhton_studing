big_table = dict()


def func(line):
    answer = line.split()
    word = answer[0]
    ip = answer[1][0:len(answer[1]) - 1]
    state = answer[2]
    status = answer[3]
    code = answer[4]
    table = dict()
    d = {ip: (word, status)}
    table.update(d)
    if ip in big_table:
        if status != 'ERROR':
            big_table[ip][word]['GOOD'] += 1
        else:
            big_table[ip][word][status] += 1
    else:
        d1 = {ip: {'POST': {'GOOD': 0, 'ERROR': 0}, 'GET': {'GOOD': 0, 'ERROR': 0}, 'PUT': {'GOOD': 0, 'ERROR': 0}}}
        big_table.update(d1)
        if status != 'ERROR':
            big_table[ip][word]['GOOD'] += 1
        else:
            big_table[ip][word][status] += 1


file = open('input.txt', 'r')
for line in file:
    func(line)
for i, j in big_table.items():
    print('ip:', i, 'POST', j['POST'], 'GET', j['GET'], 'PUT', j['PUT'])
