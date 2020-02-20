# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())
for t in xrange(T):
    string = raw_input()
    
    numOfDeletions = 0
    lastChar = None
    for i in range(len(string)):
        if lastChar == string[i]:
            numOfDeletions += 1
        else:
            lastChar = string[i]
    print numOfDeletions