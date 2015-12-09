s = r"RNBQKBNR\PPP1PPPP\8\8\8\8\pppppppp\rnbqkbnr"
for e in "12345678":
    s=s.replace(e,int(e)*" ")
s=s.replace("\\","")
print "\n"
for a in [x*8 for x in range(8)]:
    print "  "+s[a:a+8]
print "\n"

blackpieces="PNBRQK"
whitepieces="pnbrqk"


def IsAttacked(square):
    if s[square] in blackpieces:
        p,n,b,r,q,k=whitepieces
        up=-1
    elif s[square] in whitepieces:
        p,n,b,r,q,k =blackpieces
        up=1
    else:
        print "not a piece"
        return False
    # pawn
    if (s[square + 8*up + 1] == p and square%7
            or s[square + 8*up - 1] == p and square&7+1): 
        return True
    # cols
    if cols(square,up) or cols(square,-1*up):
        return True
    else:
        print p+ " Clear"
        return False

def cols(q,up):
    q = q+8*up
    sq = s[q]
    print s[q]
    if 64 > sq > -1:
        if sq in r+k+q: # hah! k!
            return True    
        elif sq == " ":
            return cols(q,up)
        else:
            return False


for i in range(64):
    print IsAttacked(i)

'''
    If color black, get pos K dir=-1, else get pos k, dir =1
    pos + (dir,-1) or (dir,1) a P?
    ((+2,-2),(+1,-1)) and transposed, N around K?
    4 dir B or Q?
    4 dir R or Q?

    

    '''
