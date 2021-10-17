import requests
import re


def task4():
    email_list = []
    url = 'http://stafflist.wmi.amu.edu.pl/'
    page = requests.get(url, stream=True)

    for line in page.iter_lines():
        email = re.search("(\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)", line.decode("utf-8").rstrip())
        if email:
            email_list.append(email.group(0))

    print(email_list)
