def queue_7(opening_hours: int) -> str:
    SIZE_QUEUE = 5
    increasing_the_queue = 1
    counter = 0
    position = 0
    while counter < opening_hours:
        if position >= SIZE_QUEUE * increasing_the_queue:
            position = 0
            increasing_the_queue *= 2
        yield person_in_queue[position // increasing_the_queue]
        counter += 1
        position += 1


person_in_queue = ['Иван', 'Матвей', 'Никита', 'Маргарита', 'Любовь']
timer = int(input())
now_queue = queue_7(timer)
for current_person in now_queue:
    print(current_person)