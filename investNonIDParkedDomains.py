import json
idDomains = {}
nonIdDomains = {}
for file in ['domainsByNewID.txt','domainsByOldID.txt']:
    with open (file) as f:
        for line in f:
            idDomains[line.rstrip()] = True

with open ('fullParkedDomains.txt') as f:
    with open ('nonIDParkedDomains.txt', 'w') as f2:
        for line in f:
            if line.rstrip() not in idDomains:
                nonIdDomains[line.rstrip()] = True
                f2.write(line)

with open ('/data1/nsrg/kwang40/fullData/2019-03-03/banners.json') as f:
    with open('nonIDParkedData.json') as f2:
        for line in f:
            data = json.loads(line.rstrip())
            if data['domain'] in nonIdDomains:
                f2.write(line)
