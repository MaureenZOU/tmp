import glob
import random
import sys
import os

directory = './'

count = 0
for filename in glob.iglob(directory + '*.jpg', recursive=True):
	if random.random() < 0.6:
		os.remove(filename)
		count += 1

print(count)
