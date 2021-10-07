def task3():
    animal_dictionary = {
        'lew': 'lion',
        'pies': 'dog',
        'kot': 'cat',
        'koń': 'horse',
        'słoń': 'elephant',
        'tygrys': 'tiger',
        'żyrafa': 'giraffe',
        'krokodyl': 'crocodile',
        'krowa': 'cow',
        'lis': 'fox'
    }

    input_word = input('Wpisz słowo: ')
    if input_word in animal_dictionary.keys():
        print('Tłumaczenie:', animal_dictionary[input_word])
    else:
        print('Brak tłumaczenia słowa:', input_word)
