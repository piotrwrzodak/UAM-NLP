from datetime import datetime
import os.path
import re
import gzip


speech_parts = {'prep': 'przyimek', 'subst': 'rzeczownik', 'adj': 'przymiotnik', 'ppron12': 'zaimek osobowy', 'adv': 'przysłówek', 'num': 'liczebnik', 'inf': 'czasownik'}


def createDictionaries():
    word_lemma_dict = {}
    lemma_part_dict = {}
    if os.path.exists('../PoliMorf-0.6.7.tab.gz'):
        with gzip.open('../PoliMorf-0.6.7.tab.gz', 'rb') as f:
            for i in f:
                m = re.match("^(\w+)\s+(\w+)\s+(\w+):", i.decode("utf-8"))
                if m:
                    word_lemma_dict.setdefault(m.group(1), frozenset([]))
                    word_lemma_dict[m.group(1)] = word_lemma_dict[m.group(1)].union([m.group(2)])
                    if m.group(1) == m.group(2):
                        lemma_part_dict[m.group(2)] = (m.group(3))
        return [True, word_lemma_dict, lemma_part_dict]
    else:
        return [False, "Can't find PoliMorf. Download it from http://zil.ipipan.waw.pl/PoliMorf"]


def convert_to_polish(result):
    translated_result = []
    for item, part in result:
        if part in speech_parts.keys():
            translated_result.append([item, speech_parts[part]])
        else:
            translated_result.append([item, "not defined: " + part])
    return translated_result


def pos_tagging(word, word_lemma, lemma_part):
    if word in word_lemma.keys():
        result = []
        for lemma in word_lemma[word]:
            result.append([lemma, lemma_part[lemma]])
        return [True, convert_to_polish(result)]
    else:
        return [False, "Word not found"]


if __name__ == "__main__":
    print([datetime.now().strftime("%H:%M:%S")], "program stared")
    output = createDictionaries()
    print([datetime.now().strftime("%H:%M:%S")], "dictionary created")
    if output[0]:
        while True:
            print('\n')
            input_word = input('Enter Polish word: ')
            if input_word == "exit":
                break
            elif re.match("^[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż\-]+$", input_word):
                result = pos_tagging(input_word, output[1], output[2])
                if result[0]:
                    for lemma, part in result[1]:
                        print(lemma, ":", part)
                else:
                    print(result[1])
            else:
                print("It's not a word.")
    else:
        print(output[1])
