f = open('input3.txt', 'r')

observations = []


def time_taker(observation):
    res = []
    _line = f.readline()
    while _line[0] != 's':
        _answer = _line.split()
        res.append([_answer[0][0:len(_answer[0]) - 1], int(_answer[1][0:len(_answer[1]) - 1])])
        _line = f.readline()
        if _line == '':
            observation.append(res)
            break
    else:
        observation.append(res)
        return _line


def sum_counter(observation):
    _sum = 0
    for i in range(len(observation[1])):
        _sum += observation[1][i][1]
    return _sum


def swap_obser(observation1, observation2):
    observation1[0], observation2[0] = observation2[0], observation1[0]
    observation1[1], observation2[1] = observation2[1], observation1[1]
    observation1[2], observation2[2] = observation2[2], observation1[2]



first_line = f.readline()
name = first_line.split()[1]
for line in f:
    answer = line.split()
    if answer[0] == 'characteristics:':
        observation = [name]
        name_line = time_taker(observation)
        if name_line is not None:
            name = str(name_line).split()[1]
        _sum = sum_counter(observation)
        observation.append(_sum / len(observation[1]))
        observations.append(observation)

for i in range(len(observations)):
    for j in range(i, len(observations)):
        if observations[j][1][0][1] < observations[i][1][0][1]:
            swap_obser(observations[j], observations[i])
        elif observations[j][1][0][1] == observations[i][1][0][1] and observations[j][2] < observations[i][2]:
            swap_obser(observations[j], observations[i])
        elif observations[j][1][0][1] == observations[i][1][0][1] and observations[j][2] == observations[i][2] \
            and len(observations[j][1]) > len(observations[i][1]):
            swap_obser(observations[j], observations[i])


for i in range(len(observations)):
    print('name:', observations[i][0])
    for j in range(len(observations[i][1])):
        print(observations[i][1][j])
    print(' ')
