# Enter your code here. Read input from STDIN. Print output to STDOUT

A = raw_input()
B = raw_input()

charFrequencyA = [0 for i in range(26)]
charFrequencyB = [0 for i in range(26)]

for c in A:
    charFrequencyA[ord(c) - ord('a')] += 1
for c in B:
    charFrequencyB[ord(c) - ord('a')] += 1

deletions = 0
for i in range(26):
    deletions += abs(charFrequencyA[i] - charFrequencyB[i])
    
print deletions