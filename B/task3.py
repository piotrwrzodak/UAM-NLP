import requests
import re
import os.path


def task3():
    profanity_wordlist = []

    url = 'https://raw.githubusercontent.com/snguyenthanh/better_profanity/master/better_profanity/profanity_wordlist.txt'
    page = requests.get(url, stream=True)
    for line in page.iter_lines():
        profanity_wordlist.append(line.decode("utf-8").rstrip())
    # print(profanity_wordlist)

    big_regex = re.compile('|'.join(map(re.escape, profanity_wordlist)))

    with open("B/task3_data.txt", 'r') as file:
        if os.path.exists('B/task3_result.txt'):
            result_file = open("B/task3_result.txt", "w")
        else:
            result_file = open("B/task3_result.txt", "x")
        for line in file:
            result_file.write(re.sub(big_regex, lambda match: "-" * len(match.group(0)), line))

    print('Task 3 done - result in task3_result.txt')
