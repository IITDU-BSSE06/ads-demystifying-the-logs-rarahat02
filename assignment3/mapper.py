#!/usr/bin/python

import sys

for line in sys.stdin:
	eachData = line.strip().split(" ")
	if len(eachData) == 10:
		data0, data1 , data2, data3, data4, data5, data6, data7, data8, data9 = eachData
		print "{0}\t{1}".format(data6, data6)
