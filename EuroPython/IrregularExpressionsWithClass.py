class Word:
    def __init__(self, protoSpell):
        def isSpell(word):
            def isSyllable(proto,n):
                vowels = "aeiou"
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
                for begin in range(len(word)): #"abc"->"3"->"012"
                    for end in range(begin+1,len(word)+1): # 0->1,3->4, -> "123"
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

            for syl in doubleSyllables(word):
                if hasDuplicate(syl,word):
                    if hasSyllableInbetween(syl,word):
                        return 1
            return 0
        self.isSpell = isSpell(protoSpell)

###############################################################

gibberish = Word("abracadabra")  
print gibberish.isSpell    
