out = open('C:\Users\Duco\Documents\CodeJam\EuroPython\A-small-practice.out','w')
inp = open('C:\Users\Duco\Documents\CodeJam\EuroPython\A-small-practice.in','r')

vowels = "AEIOU"
entries = int(inp.readline())
for x in range(entries+1):
    if x == 0:
        continue
    C = inp.readline()
    for vowel in vowels:
        if vowel == C[0]:
            Y = "a queen"
            break
        else:
            Y = "a king"
    if C[C.find("\n")-1] == 'y':
        Y = "nobody"
    C = C.strip()
    out.write("Case #" +str(x)+ ": " +C+ " is ruled by " +Y+ ".\n")
out.close()
inp.close()

