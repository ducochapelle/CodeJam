from math import atan, hypot

def pilot(t):
    if t < 10:
        return [1.,0.,0.] # gas (0-1), break (0-1), steer (-.5,.5 (pi))
    elif t < 15:
        return [0.,0.,0.]
    else:
        return [1.,0.,0.]

car_mass = 1.
car_power = lambda rev: 1-rev # with rev (0-1)
car_transmission = 1/10.

# COG wheel distances
car_left = 0.5
car_right = 0.5
car_height = 0.3 
car_front = 1.0
car_rear = 0.5
# look at that arrow

ts = 200
dt = .1

sx, sy = [0]*ts, [0]*ts
vx, vy = [0]*ts, [0]*ts
ax, ay = [0]*ts, [0]*ts
dir_rear = 0 # 0 - 2 (pi)
dir_front = 0

for t in range(ts-1):
    steer = pilot(t)[2]
    throtle = pilot(t)[0]

    sx[t+1]=vx[t]*dt+sx[t]
    sy[t+1]=vy[t]*dt+sy[t]
    vx[t+1]=ax[t]*dt+vx[t]
    vy[t+1]=ay[t]*dt+vy[t]

    F_rear = car_power(v[t]*car_transmission)*throtle

    dir_rear = atan(vy[t]/vx[t])
    dir_front = dir_rear + steer

    dir_cog = steer*car_rear/(car_rear + car_front)
    F_front_max = car_mass*0.15*9.806

    ax[t+1]=cos(dir
    print "{:0.2f}, {:.2f}, {:.2f}".format(s[t],v[t],a[t])


