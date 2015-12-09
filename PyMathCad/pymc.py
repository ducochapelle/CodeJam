
class pymc:
    pass
pymc.STMT = ";"
pymc.RTRN = "~"
#raw_input("Press Enter to continue...")
pymc.fstr = ''
pymc.line = True
pymc.f = open('sample.txt','r')
pymc.f2 = open('sample.tmp','w')

while pymc.line:
    pymc.line = pymc.f.readline()
    if pymc.line.startswith(pymc.STMT): 
        pymc.fstr += pymc.line[len(pymc.STMT)+1:] 
    if pymc.line.startswith(pymc.RTRN):
        exec pymc.fstr
        pymc.fstr = ''
        pymc.f2.write('{0} = {1}\n'.format(
            pymc.line.split("=")[0].strip(),
            eval(pymc.line[1:].split("=")[0]))
                 )
    else:
        pymc.f2.write(pymc.line)
pymc.f.close()
pymc.f2.close()

pymc.line = True
pymc.f2 = open('sample.tmp','r')
pymc.f = open('sample.txt','w')
while pymc.line:
    pymc.line = pymc.f2.readline()
    pymc.f.write(pymc.line)
pymc.f.close()
pymc.f2.close()




    
        
