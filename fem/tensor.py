class Tensor():
    def __init__(self,t,u=None):
        self.Tensor = t
        self.Rotated = None
        if u:
            self.Rotate(u)
    def Rotate(self,u):
        self.Rotated = self.mmult(self.mmult(u,self.Tensor),zip(*u))  
    def mmult(self,m1,m2):
        M = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(m2)):
            for j in range(len(m2[0])):
                for k in range(len(m1)):
                    M[i][j] += m1[i][k]*m2[k][j]
                M[i][j] = round(M[i][j])
        return M

import math
def cos(x):
    return math.cos(math.radians(x))
def sin(x):
    return math.sin(math.radians(x))

                 
a =  ((0,   0,      0)
     ,(0,   1889,   -1091)
     ,(0,   -1091,  630))
b = ((0,0,0),(0,cos(30),-sin(30)),(0,sin(30),cos(30)))
t = Tensor(a)
print t.Rotated
t.Rotate(b)
print t.Rotated

t2 = Tensor(a,b)
print t2.Rotated

