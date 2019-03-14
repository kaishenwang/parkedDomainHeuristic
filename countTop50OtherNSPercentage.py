unqiueDomains = {}
with open ('tokenNS.txt') as f:
    for line in f:
        unqiueDomains[line[:line.find(':')]] = True
print ('Token NS unqiue Domains count: ' + str(len(uniqueDomains)))

unqiueDomains = {}
with open ('otherNS.txt') as f:
    countLine = 0
    for line in f:
         countLine += 1
         if countLine == 51:
             print ('Top 50 other NS unique Domain Count: ' + str(len(unqiueDomains)))
        unqiueDomains[line[:line.find(':')]] = True
print ('Other NS unqiue Domains count: ' + str(len(uniqueDomains)))
