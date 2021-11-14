import re
import gzip


def createDictionary():
    dictionary = set()
    with gzip.open('PoliMorf-0.6.7.tab.gz', 'rb') as f:
        for i in f:
            m = re.match("([A-Za-z]+)", i.decode("utf-8"))
            if m:
                dictionary.add(m.group(0))
    return dictionary


def max_match(sentence, dictionary):
    if re.search(r"\s", sentence):
        return "sentence should not have whitespaces"
    if sentence == '':
        return []

    for i in range(len(sentence) - 1, -1, -1):
        first_word = sentence[0: i + 1]
        remainder = sentence[i + 1: len(sentence)]

        if first_word in dictionary:
            return first_word, max_match(remainder, dictionary)

    first_word = sentence[0]
    remainder = sentence[1:]
    return first_word, max_match(remainder, dictionary)


if __name__ == '__main__':
    dictionary = createDictionary()
    print(max_match("alamakota", dictionary))
