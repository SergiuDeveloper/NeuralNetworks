#!/usr/bin/python

import re

with open("Latin-Lipsum.txt") as f:
	content = f.read()

content = re.sub('[^a-zA-Z0-9\s]+', '', content)

words = content.split()
words.sort()

print(words)
