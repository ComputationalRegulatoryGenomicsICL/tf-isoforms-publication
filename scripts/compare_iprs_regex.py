#!/usr/bin/env python

import re
import sys


interproFileName1 = sys.argv[1]
interproFileName2 = sys.argv[2]
iprListFileName = sys.argv[3]


def fillDict(interproFile, iprList):
    interproDict = dict()
    state = 'interpro'
    for line in interproFile:
        if state == 'interpro':
            if '<interpro ' in line:
                iprAccession = re.search(r"id=\"(IPR[0-9]+)\"", line).group(1)
                if iprAccession in iprList:
                    state = 'name'
            else:
                continue
        elif state == 'name':
            if '<name>' in line:
                #print(line)
                iprName = re.search(r"<name>([a-zA-Z0-9/,'\s\-\(\)\.]+)</name>", line).group(1)
                state = 'abstract'
            else:
                continue
        elif state == 'abstract':
            if '<abstract>' in line:
                iprAbstract = line.strip()
                state = 'abstract_in'
            elif '<interpro ' in line: # accession does not have abstract
                interproDict[iprAccession] = [iprName, '']
                iprAccession = re.search(r"id=\"(IPR[0-9]+)\"", line).group(1)
                if iprAccession in iprList:
                    state = 'name'
                else:
                    state = 'interpro'
            else:
                continue
        else: # state == 'abstract_in'
            iprAbstract += line.strip()
            if '</abstract>' in line:
                interproDict[iprAccession] = [iprName, iprAbstract]
                state = 'interpro'
                #print(interproDict[iprAccession])
    return(interproDict)


with open(iprListFileName, 'r') as iprListFile:
    iprList = [line.strip() for line in iprListFile]

with open(interproFileName1, 'r') as interproFile1:
    interproDict1 = fillDict(interproFile1, iprList)

with open(interproFileName2, 'r') as interproFile2:
    interproDict2 = fillDict(interproFile2, iprList)

for ipr in iprList:
    if (interproDict1[ipr][0] != interproDict2[ipr][0]) or \
       (interproDict1[ipr][1] != interproDict2[ipr][1]):
        print(ipr)
