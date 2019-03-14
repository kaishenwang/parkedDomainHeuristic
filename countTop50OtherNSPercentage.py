uniqueDomains = {}
with open ('tokenNS.txt') as f:
    for line in f:
        domains = line[line.find(':')+1 : ].split(',')
        for domain in domains:
            uniqueDomains[domain] = True
print ('Token NS unqiue Domains count: ' + str(len(uniqueDomains)))

uniqueDomains = {}
with open ('otherNS.txt') as f:
    countLine = 0
    for line in f:
         countLine += 1
         if countLine == 51:
             print ('Top 50 other NS unique Domain Count: ' + str(len(uniqueDomains)))
         domains = line[line.find(':')+1 : ].split(',')
         for domain in domains:
             uniqueDomains[domain] = True
print ('Other NS unqiue Domains count: ' + str(len(uniqueDomains)))
