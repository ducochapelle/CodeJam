class S1:
	def __init__(self):
		self.last = -1
	def next(self):
		if self.last == -1:
			self.last = 1
		else:
			self.last = -1
		return self.last
s1 = S1()

class S2:
	def __init__(self):
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
		self.last = 0
	def next(self):
		self.last += 1
		return self.last
s = S()

def average_list(l):
    return reduce(lambda y,z: y+z, l)/float(len(l))

def ave(t, a, quiet=True):
	a.__init__()
	sum_a = 0
	sums_a = []
	ave_sums_a = []
	for x in range(t):
		sum_a += a.next()
		sums_a += [sum_a]
		ave_sums_a += [average_list(sums_a)]
		if not quiet:
			print sums_a, ave_sums_a, average_list(ave_sums_a)
		else:
			print average_list(ave_sums_a)
print "\ns1:", s1.next(), s1.next(), s1.next(), s1.next(), s1.next(), s1.next()
print "\ns2:", s2.next(), s2.next(), s2.next(), s2.next(), s2.next(), s2.next()
print "\ns: ", s.next(), s.next(), s.next(), s.next(), s.next(), s.next()
		    
print "\ns1: [sums], [averages of sums], average of averages of sums"
ave(12,s1, quiet=False)
print "\ns2: [sums], [averages of sums], average of averages of sums"
ave(12,s2, quiet=False)
print "\ns: [sums], [averages of sums], average of averages of sums"
ave(12,s, quiet=False)
print "\ns1: average of averages of sums"
ave(24,s1)
print "\ns2: average of averages of sums"
ave(48,s2)
print "\ns: average of averages of sums"
ave(96,s)
