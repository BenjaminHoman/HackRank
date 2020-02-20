# Enter your code here. Read input from STDIN. Print output to STDOUT

T = input()
for t in range(T):
    string = raw_input()
    if len(string) % 2 != 0:
        print -1
    else:
        str1, str2 = string[:len(string)/2], string[len(string)/2:]
        
        charFreq1, charFreq2 = [0 for i in range(26)], [0 for i in range(26)]
        
        for c in str1:
            charFreq1[ord(c) - ord('a')] += 1
        for c in str2:
            charFreq2[ord(c) - ord('a')] += 1
        
        moves = 0
        for i in range(len(charFreq1)):
            moves += abs(charFreq1[i] - charFreq2[i])
        print moves/2
        
        
        
        
        
        
        
        
        
        
        
        
        