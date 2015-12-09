s = '''head
 branch_mother_fucker
  leave
  leave
 branch
  leave'''
  
def draw(tree):
    tree = tree.split('\n')
    levels = map(lambda item: len(item)-len(item.strip())+1, tree)
    w = max(map(lambda i: len(i.strip()), tree))
    m = max(levels)   
    
    # //-----------------------------------
    #      this is probabply a function
    #   ---------------------------------//
    print tree, levels
    countdown = range(1,m+1)
    countdown.reverse()
    for h in countdown:
        out1, out2, out3 = "", "", ""
        for item, level in zip(tree, levels):
            item = item.strip()
            if level == h:
                w1 = int(w/2.)
                w2 = int(w-w1-1+w%2.)
                out1 += " +"+w1*"-"+"+"+w2*"-"+"+"
                w1 = int((w-len(item))/2)
                w2 = int(w-w1-len(item))
                out2 += " +"+w1*" "+item+w2*" "+"+"
                out3 += " +"+w*"-"+"+"
        print out1
        print out2
        print out1
    # ---------------//--------------------
        
        
    
                
        
        
        