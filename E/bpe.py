import re

from E.matchMax import max_match


def prepare_sentence(sentence):
    sentence = sentence.lower()
    punctuation_removed = re.sub('[.?!,:;\-—\[\]{}()\'"]', '', sentence)
    whitespaces_replaced = re.sub('\s+', '<w>', punctuation_removed)
    return whitespaces_replaced


def bpe_algorithm(sentence, number):
    helper_vocabulary = set()
    helper_vocabulary.add("<w>")
    sentence = prepare_sentence(sentence)

    vocabulary = {}
    matched = max_match(sentence, helper_vocabulary, [])

    for char in matched:
        if char in vocabulary:
            vocabulary[char] += 1
        else:
            vocabulary[char] = 1

    if number < len(vocabulary):
        return "\nThe minimum dictionary size ({0}) is bigger than \'number\' ({1}).\n{2} ({3} subwords)".format(
            str(len(vocabulary)), str(number), str(vocabulary), str(len(vocabulary)))

    for _ in range(number - len(vocabulary)):
        dictionary = {}
        # print(vocabulary, '(' + str(len(vocabulary)) + ' subwords)')
        for i in range(len(matched) - 1):
            bigram = matched[i] + matched[i + 1]
            if bigram in dictionary:
                dictionary[bigram] += 1
            else:
                dictionary[bigram] = 1

        for x, y in dictionary.items():
            if y == max(dictionary.values()):
                vocabulary[x] = y
                break

        matched = max_match(sentence, vocabulary.keys(), [])

    if number > len(vocabulary):
        return "\nThe maximum dictionary size ({0}) is bigger than \'number\' ({1}).\n{2} ({3} subwords)".format(
            str(len(vocabulary)), str(number), str(vocabulary), str(len(vocabulary)))
    return "\n{0} ({1} subwords)".format(str(vocabulary), str(len(vocabulary)))


if __name__ == "__main__":
    print(bpe_algorithm('Hurry on, Harry, hurry on!', 15))
