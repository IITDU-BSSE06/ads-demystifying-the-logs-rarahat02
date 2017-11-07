#!/usr/bin/python

import sys

maxValue = 0
totalSales = 0
oldKey = None
path = ""
tempFile = ""

for line in sys.stdin:
    mappedData = line.strip().split("\t")
    if len(mappedData) != 2:
        continue

    thisKey, fullFilePath = mappedData

    if oldKey and oldKey != thisKey:
        oldKey = thisKey
        if totalSales > maxValue:
            maxValue = totalSales
            tempFile = thisKey
            path = fullFilePath
        totalSales = 0

    oldKey = thisKey
    totalSales += 1

print tempFile + '\t' + path
