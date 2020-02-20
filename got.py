string = raw_input()
 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

isEvenLen = len(string) % 2 == 0
charMap = dict()

for c in string:
    if c not in charMap:
        charMap[c] = 0
    charMap[c] += 1

oddGroupsAmnt = 0
for c in charMap.keys():
    if charMap[c] % 2 != 0:
        oddGroupsAmnt += 1
        
if (isEvenLen and oddGroupsAmnt == 0) or (not isEvenLen and oddGroupsAmnt == 1):
    found = True

if not found:
    print("NO")
else:
    print("YES")