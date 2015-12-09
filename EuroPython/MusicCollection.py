def eliminate(list):
    if list == []:
        return ":("
        
    shortlist = [102*"a"] 
    lowest = 102*"a"  
    sameLengthValue = 102*256
    for word in list:    
        if len(word) < len(shortlist[0]):
            shortlist = [word]
        elif len(word) == len(shortlist[0]):
            shortlist.append(word)

    if len(shortlist) > 1:
        for word in shortlist:
            sameLengthValueRecord = sameLengthValue
            sameLengthValue = 0
            for char in word:
                sameLengthValue += ord(char)
            if sameLengthValue < sameLengthValueRecord:
                lowest = word
        return '"'+ lowest.upper() + '"'
    else:
        return '"'+ shortlist[0].upper() + '"'

def oneCase():
    albumLength = int(input.readline())
    album = range(albumLength)
    for i in range(albumLength):
        album[i] = input.readline().strip()

    for song in album:
        possibleSnippets = []
        for begin in range(len(song)):
            for end in range(begin,len(song)+1):
                snippet = song[begin:end]
                found = 0
                for song2 in album:
                    if song2 == song:
                        continue
                    if song2.find(snippet) > -1 :
                        found = 1
                        break
                if found == 0:
                    possibleSnippets.append(snippet)
        output.write(eliminate(possibleSnippets)+ "\n")
    return

input = open("C:\Users\Duco\Documents\CodeJam\EuroPython\B-small-practice.in","r")
output = open("C:\Users\Duco\Documents\CodeJam\EuroPython\B-small-practice.out","w")
# a = ord(chr(1))

cases = int(input.readline())
print str(cases) + " amount of cases"
output.write("\n")
for case in range(cases):
    output.write("Case #"+str(case+1)+":\n")
    oneCase()
    
output.close()
input.close()
print "Done"

