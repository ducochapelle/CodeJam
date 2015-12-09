class S1:
    def __init__(self):
        self.name = "s1"
        self.last = -1
    def next(self):
        self.last *= -1
        return self.last
s1 = S1()

class S2:
    def __init__(self):
        self.name = "s2"
        self.last = 0
    def next(self):
        if self.last != 0: 
            self.last =  -(self.last + self.last/abs(self.last))
        else:
            self.last = 1
        return self.last
s2 = S2()

class S:
    def __init__(self):
        self.name = "s"
        self.last = 0
    def next(self):
        self.last += 1
        return self.last
s = S()
class SminS2:
    def __init__(self):
        self.s = S()
        self.s2 = S2()
        self.last = 0
        self.name = "smins2"
    def next(self):
        self.last = self.s.next()-self.s2.next()
        return self.last
smins2 = SminS2()
    

def average_list(l):
    return reduce(lambda y,z: y+z, l)/float(len(l))

def ave(t, a):
    a.__init__()
    sum_a = 0
    sums_a = []
    ave_sums_a = []
    ave_ave_sums_a = []
    for x in range(t):
        sum_a += a.next()
        sums_a += [sum_a]
        ave_sums_a += [average_list(sums_a)]
        ave_ave_sums_a += [average_list(ave_sums_a)]
    a.__init__()    
    print "{0:16}{1:16}{2:16}{3:16}".format(a.name,
                                            "sums_"+a.name,
                                            "ave_sums_"+a.name,
                                            "ave_ave_sums_"+a.name)
    for x in range(t):
        print "{0:16}{1:16}{2:16}{3:16}".format(a.next(),
                                                sums_a[x],
                                                ave_sums_a[x],
                                                ave_ave_sums_a[x])
          

ave(144,s1)
ave(144,s2)
ave(144,s)
