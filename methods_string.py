def create_dsm() -> list:
    dsm = []
    cell_0 = {'dot': 2, 'e': 7, '+-': 1, 'digit': 1, 'end': 0}
    dsm.append(cell_0)
    cell_1 = {'dot': 2, 'e': 3, '+-': 7, 'digit': 1, 'end': 1}
    dsm.append(cell_1)
    cell_2 = {'dot': 7, 'e': 7, '+-': 7, 'digit': 4, 'end': 1}
    dsm.append(cell_2)
    cell_3 = {'dot': 7, 'e': 7, '+-': 5, 'digit': 6, 'end': 0}
    dsm.append(cell_3)
    cell_4 = {'dot': 7, 'e': 3, '+-': 7, 'digit': 4, 'end': 1}
    dsm.append(cell_4)
    cell_5 = {'dot': 7, 'e': 7, '+-': 7, 'digit': 6, 'end': 0}
    dsm.append(cell_5)
    cell_6 = {'dot': 7, 'e': 7, '+-': 7, 'digit': 6, 'end': 1}
    dsm.append(cell_6)
    cell_7 = {'dot': 7, 'e': 7, '+-': 7, 'digit': 7, 'end': 0}
    dsm.append(cell_7)
    return dsm


def get_next(dsm: dict, symb: str) -> int:
    if symb == '.':
        return dsm['dot']
    elif symb == 'e' or symb == 'E':
        return dsm['e']
    elif symb == '+' or symb == '-':
        return dsm['+-']
    elif str.isdigit(symb):
        return dsm['digit']
    else:
        return -1


def is_real_num(num: str) -> int:
    dsm = create_dsm()
    _idx = 0
    for symb in num:
        _idx = get_next(dsm[_idx], symb)
        if _idx == -1:
            return 0
    return dsm[_idx]['end']


def main():
    good_nums = ["2", "0089", "-0.1", "+3.14", "4.", "-.9",
                 "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    bad_nums = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    for num in good_nums:
        if is_real_num(num):
            print(f'Yes, {num} is real num')
        else:
            print(f'No, {num} is not real num')
    print()
    for num in bad_nums:
        if is_real_num(num):
            print(f'Yes, {num} is real num')
        else:
            print(f'No, {num} is not real num')


main()
