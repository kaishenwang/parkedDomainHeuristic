idDomains = {}

for file in ['domainsByNewID.txt','domainsByOldID.txt']:
    with open (file) as f:
        for line in f:
            idDomains[line.rstrip()] = True

with open ('fullParkedDomains.txt') as f:
    with open ('nonIDParkedDomains.txt', 'w') as f2:
        for line in f:
            if line.rstrip() not in idDomains:
                f2.write(line)

        
