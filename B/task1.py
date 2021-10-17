import re


def task1():
    first_uppercase = re.compile("^[A-Z]")

    name = input('Enter name: ')
    name_result = first_uppercase.match(name)
    if name_result is None:
        print('Name should start with uppercase letter.')

    surname = input('Enter surname: ')
    surname_result = first_uppercase.match(surname)
    if surname_result is None:
        print('Surname should start with uppercase letter.')

    phone_number = input('Enter phone number: ')
    phone_number_result = re.match("\(\d{2}\)\s\d{3}-\d{2}-\d{2}", phone_number)
    if phone_number_result is None:
        print('Phone number should be in format: (XX) XXX-XX-XX')

    zip_code = input('Enter ZIP code: ')
    zip_code_result = re.match('\d{2}-\d{3}', zip_code)
    if zip_code_result is None:
        print('ZIP code should be in format: XX-XXX')

    city = input('Enter city: ')
    city_result = first_uppercase.match(city)
    if city_result is None:
        print('City name should start with uppercase letter.')
