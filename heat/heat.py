import sympy.physics.units as u
import random
from math import *
# http://www.engineeringtoolbox.com/overall-heat-transfer-coefficient-d_434.html

Di = 800*u.mm
Ai = Di**2*pi/4.
t = 15*u.mm

flow = 400e6*u.feet**3/u.day
pres = 60
v = flow/pres/Ai

h_g = sqrt(100/10)*10*u.W/u.m**2/u.K
h_w = sqrt(10000/500)*500*u.W/u.m**2/u.K
k_s = sqrt(24/16)*16*u.W/u.m/u.K

U_g = 1/(1/h_g + t/k_s + 1/h_g)
U_w = 1/(1/h_w + t/k_s + 1/h_g)

# what about a distribution where the average 
# outcome is a*sqrt(b/a), instead.
def dist(a,b):
	mean = a*.5+b*.5
	stdd = mean-min(a,b)
	return random.gauss(mean, stdd/2)

U_gs, U_ws = [], []
for n in range(1):
	h_w = dist(500,10000)*u.W/u.m**2/u.K
	h_g = dist(10,100)*u.W/u.m**2/u.K
	k_s = dist(16,24)*u.W/u.m/u.K
	U_gs.append( 1/(1/h_g + t/k_s + 1/h_g) )
	U_ws.append( 1/(1/h_w + t/k_s + 1/h_g) )

print U_g, U_w

