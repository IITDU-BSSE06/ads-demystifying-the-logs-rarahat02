#!/usr/bin/python

import sys

counter = 0

for line in sys.stdin:
	dataMapped = line.strip().split("\t")
	if len(dataMapped) != 2:
		continue
	ip, restOfData = dataMapped
	if ip =='10.99.99.186':
		counter = counter + 1
print str(counter)
