import os

name_splitters = ' _-.,()[]!?'
name_splitters = [chr(x) for x in range(32,48)+range(58,65)+range(91,97)+range(123,127)]

def NameSplitter(s)
    #RECURSE THIS SHIT
    s.split(name_splitters[n])
def UpperWhenLower(s):
    '''returns a list of strings. The input string is chopped where
    CamelCase -> Camel Case.'''
    case, last_case, new_s = "","",""
    for c in s:
        if ord(c) in range(65,91):
            case = "upper"
        elif ord(c) in range(97,123):
            case = "lower"
        else:
            new_s += c
            continue
        if last_case == "lower" and case == "upper":
            new_s += "_"+c
        else:
            new_s += c
        last_case = case
    return new_s.split('_')
def SplitPath(s):
    return s.split(os.path.sep)
def UpperLowerMayhem(s):
    '''returns a list of strings:
    CamelABCase -> Camel ABC Case ase'''
def NumberLetter(s):
    '''returns a list of strings:
    Appelpie1243whatever -> Appelie 1243 whatever'''
    case, last_case, new_s = "","",""
    for c in s:
        if ord(c) in range(48,58):
            case = "number"
        elif ord(c) in range(97,123)+range(65,91):
            case = "letter"
        else:
            new_s += "_"+c+"_"
            continue
        if last_case != case:
            new_s += "_"+c
        else:
            new_s += c
        last_case = case
    return new_s.split('_')


#get all paths as keys in a dict
#for all path, chop it up with the name splitters
#chop the chopped up parts up with the upper_when_lower and number_when_letter
paths = []
for root, dirs, files in os.walk('C:\Users\Duco\Downloads\~1'):
    for file in files:
        paths.append(os.path.join(root,file))

chops = []
for path in paths:
    for part1 in SplitPath(path):
        for c in name_splitters:
            for part2 in part1.split(c):
                for part3 in UpperWhenLower(part2):
                    chops.append(part3)
chopset = set(chops)
                