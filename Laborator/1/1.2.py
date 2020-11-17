#!/usr/bin/python

import re


def order_words(content):
    content = re.sub(r'[^a-zA-Z0-9\s]+', '', content)

    words = content.split()
    words.sort()

    return words


if __name__ == '__main__':
    with open("Latin-Lipsum.txt") as f:
        content = f.read()

    words = order_words(content)
    print(words)
