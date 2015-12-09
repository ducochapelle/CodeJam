import random

def Spawn(id):
    x = random.randint(0,9)
    y = random.randint(0,9)
    if area[x][y].presence == []:
        area[x][y].presence.append(id)
        return [x,y]
    else:
        Spawn(id)

def Name(kind):
    if kind == "human":
        f = open("names.txt",'r')
        name = ""
        for i in range(random.randint(1,1000)):
            name = f.readline().rstrip(' \n')
        f.close()
        return name[0:7]
    if kind == "zombie":
        if random.randint(1,2)==1:
            return "GREG"
        else:
            return "BUTCH"

def Monitor(token):
    for y in area:
        row = ""
        for x in y:
            if x.presence == []:
                row += "."
            else:
                row += str(x.presence[0])
        print row

def MonitorOld(area):
    for y in area:
        row = ""
        for x in y:
            if x.presence == []:
                row += " ".ljust(8)
            else:
                row += people[x.presence[0]].name.ljust(8)
        print row
        row = ""
        for x in y:
            if x.presence == []:
                row += " ".ljust(8)
            else:
                row += str(x.presence).ljust(8)
        print row
        row = "" 
        for x in y:
            if x.soundId == []:
                row += " ".ljust(8)
            else:
                row += str(x.soundId).ljust(8)
        print row
            

class Person():
    def __init__(self,kind):
        self.kind = kind
        self.name = Name(kind)
        self.id = len(people)
        self.location = Spawn(self.id)
        self.humanScent = [0,0]
        self.zombieScent = [0,0]
        self.noise = [0,0]
    def emit(self):
        area[self.location[0]][self.location[1]].smell = self.kind
        area[self.location[0]][self.location[1]].smellId = self.id
        for x in range(-1,2):
            for y in range(-1,2):
                try:
                    area[self.location[0]+x][self.location[1]+y].sound = "light"
                    area[self.location[0]+x][self.location[1]+y].soundId.append(self.id)
                except IndexError:
                    print "outside area..."
    def sense(self):
        self.humanScent = [0,0]
        self.zombieScent = [0,0]
        self.noise = [0,0]
        for x in range(-1,2):
            for y in range(-1,2):
                try:
                    if area[self.location[0]+x][self.location[1]+y].sound == "light":
                        if len(area[self.location[0]+x][self.location[1]+y].soundId) > 1:
                            self.noise[0] += x
                            self.noise[1] += y
                    if area[self.location[0]+x][self.location[1]+y].smell == "human":
                        if area[self.location[0]+x][self.location[1]+y].smellId != self.id:
                            self.humanScent[0] += x
                            self.humanScent[1] += y
                    if area[self.location[0]+x][self.location[1]+y].smell == "zombie":
                        if area[self.location[0]+x][self.location[1]+y].smellId != self.id:
                            self.zombieScent[0] += x
                            self.zombieScent[1] += y
                except IndexError:
                    print "outside area..."
        if self.humanScent[0] > 0:
            self.humanScent[0] = 1
        elif self.humanScent[0] < 0:
            self.humanScent[0] = -1
        if self.humanScent[1] > 0:
            self.humanScent[1] = 1
        elif self.humanScent[1] < 0:
            self.humanScent[1] = -1
        if self.noise[0] > 0:
            self.noise[0] = 1
        elif self.noise[0] < 0:
            self.noise[0] = -1
        if self.noise[1] > 0:
            self.noise[1] = 1
        elif self.noise[1] < 0:
            self.noise[1] = -1
        if self.zombieScent[0] > 0:
            self.zombieScent[0] = 1
        elif self.zombieScent[0] < 0:
            self.zombieScent[0] = -1
        if self.zombieScent[1] > 0:
            self.zombieScent[1] = 1
        elif self.zombieScent[1] < 0:
            self.zombieScent[1] = -1
        
            
    def act(self):
        if self.kind == "human":
            if self.zombieScent != [0,0]:
                area[self.location[0]][self.location[1]].presence.remove(self.id)
                self.location[0] -= self.zombieScent[0]
                self.location[1] -= self.zombieScent[1]
                area[self.location[0]][self.location[1]].presence.append(self.id)

        if self.kind == "zombie":
            if self.humanScent != [0,0]:
                area[self.location[0]][self.location[1]].presence.remove(self.id)
                self.location[0] += self.humanScent[0]
                self.location[1] += self.humanScent[1]
                area[self.location[0]][self.location[1]].presence.append(self.id)
            elif self.noise != [0,0]:
                area[self.location[0]][self.location[1]].presence.remove(self.id)
                self.location[0] += self.noise[0]
                self.location[1] += self.noise[1]
                area[self.location[0]][self.location[1]].presence.append(self.id)

                
        
class Location():
    def __init__(self):
        self.presence = []
        self.smell = "none"
        self.smellId = "none"
        self.sound = "none"
        self.soundId = []
        
area = [[Location() for x in range(10)] for y in range(10)]   

def clear(area):
    for row in area:
        for loc in row:
            loc.sound = "none"
            loc.soundId = []
            for id in loc.presence:
                if people[id].kind == "zombie":
                    for id in loc.presence:
                        if people[id].kind == "human":
                            loc.presence.remove(id)
                            people.remove(id)
     
people = []
people.append(Person("zombie"))
people.append(Person("human"))
people.append(Person("human"))
people.append(Person("human"))
people.append(Person("human"))
people.append(Person("human"))
people.append(Person("human"))
people.append(Person("human"))

for person in people:
    person.emit()
Monitor(area)
        
def Update():
    for person in people:
        person.sense()
    for person in people:
        person.act()
    clear(area)
    for person in people:
        person.emit()
    Monitor(area)


