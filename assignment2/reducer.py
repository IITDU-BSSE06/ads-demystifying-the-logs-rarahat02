#!/usr/bin/python

import sys

counter = 0

for line in sys.stdin:
	mappedData = line.strip().split("\t")
	if len(mappedData) != 2:
		continue
	ip, restOfData = mappedData
	if '/assets/js/the-associates.js' in restOfData:
		counter = counter + 1

print str(counter)
