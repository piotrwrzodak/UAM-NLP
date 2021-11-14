import os.path
import re
import gzip


def createDictionary():
    dictionary = set()
    if os.path.exists('PoliMorf-0.6.7.tab.gz'):
        with gzip.open('PoliMorf-0.6.7.tab.gz', 'rb') as f:
            for i in f:
                m = re.match("([A-Za-z]+)", i.decode("utf-8"))
                if m:
                    dictionary.add(m.group(0))
        return True, dictionary
    else:
        return False, "Can't find PoliMorf. Download it from http://zil.ipipan.waw.pl/PoliMorf"


def max_match(sentence, dictionary, word_list):
    if re.search(r"\s", sentence):
        return "sentence should not have whitespaces"
    if sentence == '':
        return word_list

    for i in range(len(sentence) - 1, -1, -1):
        first_word = sentence[0: i + 1]
        remainder = sentence[i + 1: len(sentence)]

        if first_word in dictionary:
            word_list.append(first_word)
            return max_match(remainder, dictionary, word_list)

    first_word = sentence[0]
    remainder = sentence[1:]
    word_list.append(first_word)
    return max_match(remainder, dictionary, word_list)


if __name__ == '__main__':
    success, dictionary = createDictionary()
    if success:
        print(max_match("alamakota", dictionary, []))
    else:
        print(dictionary)
