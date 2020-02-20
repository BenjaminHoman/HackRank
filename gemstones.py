# Enter your code here. Read input from STDIN. Print output to STDOUT

foundElementsPerRock = dict()

numberOfRocks = input()
for t in xrange(numberOfRocks):
    rock = raw_input()
    
    uniqueElementsInRock = set()
    for element in rock:
        if element not in uniqueElementsInRock:
            if element not in foundElementsPerRock:
                foundElementsPerRock[element] = 0
            foundElementsPerRock[element] += 1
            uniqueElementsInRock.add(element)

gemElementsAmnt = 0
for element in foundElementsPerRock.keys():
    if foundElementsPerRock[element] == numberOfRocks:
        gemElementsAmnt += 1
        
print gemElementsAmnt