#!/usr/bin/python

import sys

maximumFileHitValue = 0
totalSales = 0
oldKey = None
path = ""
tempFile = ""



for line in sys.stdin:
    mappedData = line.strip().split("\t")
    if len(mappedData) != 2:
        continue

    thisKey, fullPath = mappedData

    if oldKey and oldKey != thisKey:
        oldKey = thisKey
        if totalSales > maximumFileHitValue:
            maximumFileHitValue = totalSales
            tempFile = thisKey
            path = fullPath
        totalSales = 0

    oldKey = thisKey
    totalSales += 1

print str(maximumFileHitValue)
