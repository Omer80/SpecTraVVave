from __future__ import division
import math
import numpy as np
import solver
import init_data
import dynamic_code
import equation as eq
from matplotlib.pyplot import plot, show

             ###### testing the solver.py functions

# basic parameters' values to initiate computation
N = 64          #number of nodes 
L = math.pi     #half of the wave length 
eps = 0.1
#Equation = Whitham
#speed = eq.Whitham.speed()    #phase speed
#u0 = eq.Whitham(N, L, speed).init_guess()    #-0.015-0.1*np.cos(x_nodes) # initial guess
data = init_data.init_data(eq.Whitham(N, L, 1))
(u0, speed) = data.compute_init_guess()
            
            
            # solutions with given parameters

solver_kind = 'compute_fsolve'
#solver_kind = 'compute_newton'

us = []

print solver_kind

# solution via Netwon method
u = u0
c = speed
for i in range(10):
    #print i
    c += -0.0025
    #if c < 0:
     #   break
    wave = solver.solver(eq.Whitham(N, L, c), u)
    u = getattr(wave, solver_kind)()
    us.append(u)
else:
    print 'not stopped at zero'

print solver_kind, ' \n', u
plot(eq.Whitham(N, L, speed).nodes, u0)
aus = np.array(us)
for i in range(10):
    plot(eq.Whitham(N, L, speed).nodes, aus[i,:])
    
show()

dyn = dynamic_code.dynamic_code(eq.Whitham(N, L, c), u)
translated_wave = dyn.evolution()