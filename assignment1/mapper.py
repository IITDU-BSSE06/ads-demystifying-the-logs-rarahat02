#!/usr/bin/python

import sys

for line in sys.stdin:
	eachData = line.strip().split(" - - ")
	if len(eachData) == 2:
		ip, restOfData = eachData
		print "{0}\t{1}".format(ip, restOfData)
