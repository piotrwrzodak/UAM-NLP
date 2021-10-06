from random import randrange

def task2():

    # lista kwadratów liczb naturalnych z przedziału [0,50]
    first_list = []
    for i in range(0, 51):
        first_list.append(i * i)
    print(first_list)

    # sześciany liczb naturalnych z zakresu 20 do 30
    second_list = []
    for j in range(20, 31):
        second_list.append(pow(j, 3))
    print(second_list)

    # wartości funkcji 3x-2 na liczbach całkowitych przedziale od -5 do 5
    third_list = []
    for k in range(-5, 6):
        third_list.append(3 * k - 2)
    print(third_list)

    # pary (x,y), gdzie x jest liczbą naturalną z zakresu 10-20, a y liczbą naturalną z zakresu 5-10
    fourth_list = []
    for l in range(randrange(4, 7)):
        fourth_list.append('(' + str(randrange(10, 21)) + ',' + str(randrange(5, 11)) + ')')
    print(fourth_list)

    # Lista par(x, y), gdzie x jest liczbą całkowitą z przedziału[4, 7], a y jednym znapisów 'jabłko', 'gruszka' lub 'komputer'
    option_list = ['jabłko', 'gruszka', 'komputer']
    fifth_list = []
    for m in range(randrange(4, 7)):
        fifth_list.append('(' + str(randrange(4, 8)) + ',' + option_list[randrange(3)] + ')')
    print(fifth_list)
