import json
from collections import defaultdict

IDs = []
allParkedDomains = {}
newNS = defaultdict(list)
NSwithSepcialWords = {}
errorStr = '\"http\":{}},\"error\":'

def compareStrNoContain(s1, s2):
    return s2.find(s1) == -1

def parseRR(line):
    data = json.loads(line)
    try:
        hostName = data['name']
        if hostName not in allParkedDomains or data['status'] == 'NO_ANSWER':
            return
        ts = []
        if len(data['trace']) > 3:
            ts.append (data['trace'][-2])
        if len(data['trace']) > 0:
            ts.append (data['trace'][-1])
        tmp = {}
        for t in ts:
            for auth in t['results']['authorities']:
                if compareStrNoContain(auth['name'], hostName):
                    tmp[auth['name']] = True
                if compareStrNoContain(auth['answer'], hostName):
                    tmp[auth['answer']] = True
        for dm in tmp.keys():
            if dm not in NSwithSepcialWords:
                newNS[dm].append(hostName)
    except:
        return

def writeResult(fName, d):
    with open(fName, 'w') as f:
        for k,v in d:
            f.write(k + ':')
            for idx in range(len(v)-1):
                f.write(v[idx] + ',')
            f.write(v[-1] + '\n')

# find all domains found by ID
with open('domainsByOldID.txt') as f:
    for line in f:
        allParkedDomains[line.rstrip()] = True
with open('domainsByNewID.txt') as f:
    for line in f:
        allParkedDomains[line.rstrip()] = True

# find all NS with special words
with open ('NSwithSepcialWords.txt') as f:
    for line in f:
        NSwithSepcialWords[line.rstrip()] = True

# find new NS by domains
with open ('/data1/nsrg/kwang40/fullData/2019-03-03/RR.json') as f:
    for line in f:
        parseRR(line)
for k,v in newNS.items():
    newNS[k] = list(set(v))
print ('Finish Reading NS.')

sorted_NS = sorted(newNS.items(), key=lambda x: len(x[1]), reverse=True)
writeResult('newNSbyID.txt', sorted_NS)
