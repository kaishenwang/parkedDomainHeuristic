import sys
#python getDomainsByID.py oldID.txt domainsByOldID.txt
#python getDomainsByID.py newID.txt domainsByNewID.txt
uniqueDomains = {}
IDs = []

errorStr = '\"http\":{}},\"error\":'
htmlEscapeDict = {}
def encodeHtmlEscape(s):
    for i, j in htmlEscapeDict.iteritems():
        s = s.replace(i, j)
    return s

def parseZgrabJson(line):
    if line.find(errorStr) != -1:
        return
    hostNameStart = line.find('domain') + 9
    hostNameEnd = line.find('\"', hostNameStart)
    hostName = line[hostNameStart:hostNameEnd]
    for ID in IDs:
        if line.find(ID) != -1:
            uniqueDomains[hostName] = True

htmlEscapeDict['\"'] = '\\\"'
htmlEscapeDict['<'] = '\\u003c'
htmlEscapeDict['>'] = '\\u003e'
htmlEscapeDict['&'] = '\\u0026'

#read IDs
with open(sys.argv[1]) as f:
    lines = f.readlines()
IDs = [encodeHtmlEscape(line.rstrip()) for line in lines]

# find all domains found by ID
with open('/data1/nsrg/kwang40/fullData/2019-03-03/banners.json') as f:
    for line in f:
        if len(line) > 6:
            parseZgrabJson(line)

with open(sys.argv[2], 'w') as f:
    for domain in uniqueDomains.keys():
        f.write(domain + '\n')
