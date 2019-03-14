import sys
from collections import defaultdict

#python findAdditionDomainByNewID.py domainByTokenAndOtherNS.txt newID.txt  /data1/nsrg/kwang40/fullData/2019-03-03/banners.json additionDomainByNewID.txt
IDs = []
parkedDomains = {}
newDomains = defaultdict(list)

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
            newDomains[ID].append(domain)


htmlEscapeDict['\"'] = '\\\"'
htmlEscapeDict['<'] = '\\u003c'
htmlEscapeDict['>'] = '\\u003e'
htmlEscapeDict['&'] = '\\u0026'


with open (sys.argv[1]) as f:
    lines = f.readlines()
for line in lines:
    parkedDomains[line.rstrip()] = True

with open (sys.argv[2]) as f:
    lines = f.readlines()
for line in lines:
    IDs.append(encodeHtmlEscape(line.rstrip()))


with open(sys.argv[3]) as infile:
    for line in infile:
        if line[:7] == '{\"ip\":\"':
            domainNameStart = line.find('domain') + 9
            domainNameEnd = line.find('\"', domainNameStart)
            domainName = line[domainNameStart : domainNameEnd]
            if domainName not in parkedDomains:
                parse(line, domainName)

for k,v in newDomains.items():
    newDomains[k] = list(set(v))

with open (sys.argv[4], 'w') as f:
    for ID in IDs:
        f.write(ID + ':')
        for domain in newDomains[ID]:
            f.write(domain + ',')
        f.write('\n')
