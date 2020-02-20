# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())
for x in xrange(T):
    S = raw_input()
    R = S[::-1]
    
    isFunny = True
    for i in range(1, len(S)):
        isFunny &= abs(ord(S[i]) - ord(S[i-1])) == abs(ord(R[i]) - ord(R[i-1]))
    
    if isFunny:
        print "Funny"
    else:
        print "Not Funny"
    