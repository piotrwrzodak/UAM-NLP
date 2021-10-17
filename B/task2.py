import re


def task2():
    pattern = re.compile('^.+;[-+]?[0-9]+;[-+]?[0-9]+$')
    with open("B/task2_data.csv", 'r') as file:
        for line in file:
            if pattern.match(line.rstrip()) is None:
                print('Wrong format.')
                return False
    print('Good format.')
    return True
