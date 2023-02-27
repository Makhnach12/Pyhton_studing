import json
from functools import cmp_to_key


def star_comporator(a):
    x = list(a['stats'].values())
    return sum(x) / len(x)


def compare(a, b):
    if list(a['stats'].keys())[0] < list(b['stats'].keys())[0]:
        return -1
    elif list(a['stats'].keys())[0] > list(b['stats'].keys())[0]:
        return 1
    elif list(a['stats'].keys())[0] == list(b['stats'].keys())[0]:
        if star_comporator(a) < star_comporator(b):
            return -1
        elif star_comporator(a) > star_comporator(b):
            return 1
        elif star_comporator(a) == star_comporator(b):
            if list(a['stats'].values())[0] < list(b['stats'].values())[0]:
                return 1
            elif list(a['stats'].values())[0] < list(b['stats'].values())[0]:
                return -1
            else:
                return 0


with open('resources.json', 'r') as f:
    text = json.load(f)

s = sorted(text, key=lambda a: list(a['stats'].values())[0], reverse=True)
s = sorted(s, key=star_comporator)
s = sorted(s, key=lambda a: list(a['stats'].keys())[0])

text.sort(key=cmp_to_key(compare))
print(s)
print(text)


with open('results.json', 'w') as f:
    json.dump(text, f, indent=2)
