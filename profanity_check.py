"""
check profanity word in text
"""

# -*- coding: UTF-8 -*-

from urllib.request import urlopen
import urllib.parse

def read_text():
    with open('profanity.txt', 'r') as f:
        content = f.read()
        #print(content)
        check_profanity(content)


def check_profanity(text_to_check):
    encoded_text = urllib.parse.quote(text_to_check, 'utf-8')
    connection = urlopen("http://www.wdylike.appspot.com/?q=" + encoded_text)
    output = connection.read().decode('utf-8')
    print(output)
    connection.close()
    if 'true' in output:
        print("Profanity Alert!!!")
    elif 'false' in output:
        print("Great, happy to continue.")
    else:
        print("Can not scan the text properly.")

read_text()
