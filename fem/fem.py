input = open("input.txt",'r')
lines = input.readlines()

execfile("input.txt")
print str(db)

# element has E and A matprop
# element has L modelprop
# F acts in direction on element
# elongation: dL = FL/EA

# with current force.; calc position of every node as if free
#   average of elements + world
# put back nodes which were not free
# iterate

# with current position; calc f...

for n in db["elems"]
    elem = elems[n]
    abs(db["position"][elem[0]]-db["position"][elem[0]]
    # lolwut!