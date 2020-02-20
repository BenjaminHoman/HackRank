# Enter your code here. Read input from STDIN. Print output to STDOUT

s = raw_input()

unique = set()

for c in s:
    if c != " ":
        unique.add(c.lower())
    
if len(unique) >= 26:
    print "pangram"
else:
    print "not pangram"