out = open('C:\Users\Duco\Documents\CodeJam\EuroPython\C-small-practice.out','w')
inp = open('C:\Users\Duco\Documents\CodeJam\EuroPython\C-large-practice.in','r')

vowels = "aeiou"




def isSyllable(proto,n):
    hasVowel = 0
    for elem in proto:
        if elem in vowels:
            hasVowel += 1
    if hasVowel == n:
        return proto
    else:
        return 0


def doubleSyllables(word):
    list = []
    for begin in range(len(word)):
        for end in range(begin+1,len(word)+1):
            protoSyllable = word[begin:end]
            if isSyllable(protoSyllable,2):
                list.append(protoSyllable)
    return list

def hasDuplicate(syllable,word):
    if syllable in word[word.find(syllable)+len(syllable):]:
        return syllable
    else:
        return 0

def hasSyllableInbetween(syllable,word):
    begin = word.find(syllable) + len(syllable)
    end = begin + word[begin:].find(syllable)
    return isSyllable(word[begin:end],1)

cases = int(inp.readline().strip())
print cases
for i in range(1,cases+1):
    isSpell = 0
    word = inp.readline().strip()
    for syl in doubleSyllables(word):
        if hasDuplicate(syl,word):
            mid = hasSyllableInbetween(syl,word)
            if mid:
                print "Case #"+ str(i)+": "+syl+" "+mid+" "+syl
                isSpell = 1
    if not isSpell:
        print "Case #" + str(i) + ": Nothing. ------->" + word 
out.close()
inp.close()
print "Done"
