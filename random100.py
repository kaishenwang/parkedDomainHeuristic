parkedDomains = {}
with open('fullParkedDomains.txt') as f:
    for line in f:
        parkedDomains[line.rstrip()] = True

count = 0
lineCount = 0
with open('validDomains.txt') as f:
    for line in f:
        lineCount += 1
        if count == 100:
            break
        if lineCount % 800 != 0:
            continue
        if line.rstrip() not in parkedDomains:
            count += 1
            print(line.rstrip())
