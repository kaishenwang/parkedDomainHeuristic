uniqueDomains = {}

def helper(fName):
    with open(fName) as f:
        for line in f:
            uniqueDomains[line.rstrip()] = True
helper('domainsByNewID.txt')
helper('domainsByOldID.txt')
helper('domainsByAdditionID.txt')
helper('domainByTokenAndOtherNS.txt')

# New NS
newNS = {}
with open('newNS.txt') as f:
    for line in f:
        newNS[line.rstrip()] = True

with open ('newDomainsByNSTop50.txt') as f:
    for line in f:
        nsName = line[:line.find(':')]
        if nsName not in newNS:
            continue
        domainsList = line[line.find(':') + 1 : ].split(',')
        for domain in domainsList:
            uniqueDomains[domain] = True

with open('fullParkedDomains.txt', 'w') as f:
    for domain in uniqueDomains.keys():
        f.write(domain + '\n')
