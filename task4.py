import re
import os.path


def cipher_letter():
    with open('letter.txt', 'r') as letter:
        line_number = 1
        if os.path.exists('letter_ciphered.txt'):
            letter_ciphered = open("letter_ciphered.txt", "w")
        else:
            letter_ciphered = open("letter_ciphered.txt", "x")
        for line in letter:
            if line_number % 3 == 0 or re.search('kocham', line, re.I):
                letter_ciphered.write('*' * (len(line) - 1) + '\n')
            else:
                letter_ciphered.write(line)
            line_number += 1
    print('Letter ciphered.')
