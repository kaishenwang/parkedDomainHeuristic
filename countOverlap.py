oldDomains = {}
with open('domainByTokenAndOtherNS.txt') as f:
    for line in f:
        oldDomains[line.rstrip()] = True        
print('Old Domains: ' + str(len(oldDomains)))

overLapCount = 0
with open('domainsByNewID.txt') as f:
    for line in f:
        domain = line.rstrip()
        if domain in oldDomains:
            overLapCount += 1
print ('Overlap count is ' + str(overLapCount))
