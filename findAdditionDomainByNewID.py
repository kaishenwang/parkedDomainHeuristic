import sys
from collections import defaultdict

#python findAdditionDomainByNewID.py
IDs = []
parkedDomains = {}
allParkedDomains = {}
newDomains = defaultdict(list)
allDomains = defaultdict(list)
errorStr = '\"http\":{}},\"error\":'
htmlEscapeDict = {}
def encodeHtmlEscape(s):
    for i, j in htmlEscapeDict.iteritems():
        s = s.replace(i, j)
    return s

def parse(line, domain):
    if line.find(errorStr) != -1:
        return
    for ID in IDs:
        if line.find(ID) != -1:
            allDomains[ID].append(domain)
            allParkedDomains[domain] = True
            if domainName not in parkedDomains:
                newDomains[ID].append(domain)


htmlEscapeDict['\"'] = '\\\"'
htmlEscapeDict['<'] = '\\u003c'
htmlEscapeDict['>'] = '\\u003e'
htmlEscapeDict['&'] = '\\u0026'


with open ('domainByTokenAndOtherNS.txt') as f:
    lines = f.readlines()
for line in lines:
    parkedDomains[line.rstrip()] = True

with open ('newID.txt') as f:
    lines = f.readlines()
for line in lines:
    IDs.append(encodeHtmlEscape(line.rstrip()))


with open('/data1/nsrg/kwang40/fullData/2019-03-03/banners.json') as infile:
    for line in infile:
        if line[:7] == '{\"ip\":\"':
            domainNameStart = line.find('domain') + 9
            domainNameEnd = line.find('\"', domainNameStart)
            domainName = line[domainNameStart : domainNameEnd]
            parse(line, domainName)

for k,v in newDomains.items():
    newDomains[k] = list(set(v))
for k,v in allDomains.items():
    newDomains[k] = list(set(v))

with open ('additionDomainByNewID.txt', 'w') as f:
    for ID in IDs:
        f.write(ID + ':')
        for domain in newDomains[ID]:
            f.write(domain + ',')
        f.write('\n')

with open ('allDomainByNewID.txt', 'w') as f:
    for ID in IDs:
        f.write(ID + ':')
        for domain in allDomains[ID]:
            f.write(domain + ',')
        f.write('\n')

with open ('domainByNewIDCount.txt', 'w') as f:
    for ID in IDs:
        f.write(ID + ':' + str(len(allDomains[ID])) + '\n')

with open ('domainsByNewID.txt', 'w') as f:
    for domain in allParkedDomains.keys():
        f.write(domain + '\n')
