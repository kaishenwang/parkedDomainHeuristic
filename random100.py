parkedDomains = {}
with open('fullParkedDomains.txt') as f:
    for line in f:
        parkedDomains[line.rstrip()] == True

count = 0
lineCount = 0
with open('validDomains.txt') as f:
    if count == 100:
        break
    for line in f:
        if lineCount % 800 != 0:
            continue
        if line.rstrip() not in parkedDomains:
            print(line.rtrip())
