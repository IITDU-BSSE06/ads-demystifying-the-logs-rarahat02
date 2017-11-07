#!/usr/bin/python

import sys

numberOfUniqueFiles = 0
oldKey = None

for line in sys.stdin:
    mappedData = line.strip().split("\t")
    if len(mappedData) != 2:
        continue

    thisKey, fullPath = mappedData



    if oldKey and oldKey != thisKey:
        numberOfUniqueFiles += 1
        oldKey = thisKey;
        salesTotal = 0
    oldKey = thisKey



print str(numberOfUniqueFiles)
