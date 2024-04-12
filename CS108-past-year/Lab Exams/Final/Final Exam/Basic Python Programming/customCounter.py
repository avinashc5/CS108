import os
import sys

if len(sys.argv) == 1:
	print('File name not provided')
	print('Usage: python3 customCounter.py <file>')
	exit()

filename = sys.argv[1]

with open(filename) as f:
	text = f.read()
	count = {}
	for c in text:
		if c not in count.keys():
			count[c] = 1
		else:
			count[c] += 1

for c in count.keys():
	print(f'{c}:{count[c]}')