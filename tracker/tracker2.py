import math
samples = 100
res = 10.

class World():
    def __init__(self):
        self.dimensions = 2
        self.speedlimit = 5.
        self.steerlimit = 60/180*math.pi
        self.friction = 0.2
        self.g = 9.81
world = World()    

class Car():
    def __init__(self):
        self.m = 10
        dimension = [0.]*world.dimensions
        self.s = [0.]*world.dimensions
        self.v = [0.]*world.dimensions
        self.a = [0.]*world.dimensions
        self.aim = [1.]+[0.]*(world.dimensions-1)
        self.steer = 1 # 1=cw , -1=ccw
        self.gas = 1.
    def mapNM(self,d):
        return math.cos(0.5*self.v[int(d)]/world.speedlimit*math.pi)
    def update(self):
        self.vm = reduce(math.hypot,self.v)
        world.g*world.friction*self.m == 0
        .5 * self.m * self.vm**2 == self.a * self.m
        for d in range(world.dimensions):
            self.a[d] = self.mapNM(d) * self.gas * self.aim[d]
            self.v[d]+=self.a[d]/res
            self.s[d]+=self.v[d]/res
car = Car()

class Display():
    def __init__(self):
        self.cols, self.rows = 70,70
        self.m = ("."*self.cols+"\n")*self.rows
    def update(self,s):
        changeling = int(s[0]+self.cols*s[1])
        print changeling
        self.m = self.m[:changeling]+"+"+self.m[changeling+1:]
    def display(self):
        print self.m
display = Display ()    
#class Driver():
#   def __init__(self):
#      self.
for t in range(samples):
    print map(lambda x: round(x[0],2), [car.a, car.v, car.s])
    car.update()
    display.update(car.s)
display.display()    
    