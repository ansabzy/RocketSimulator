###importing libraries needed to build model
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

###this will be a flat Earth model
##Mainly diving into physics and math operatiosn through python
##the trajectory of an object (rocket) will be determined. More might be added later

#rocket
mass = 40 #g

###equation
## F= m*a aka F=m*second derivative of displacement
## z will be the displacement of objecet above surface (in m)
## dzdt is the velocity, dzzdt is the acceleration

### state vector - like a snapshot of the projectile at a single moment
##second order differentiual equation = two states
def statederivative (state, t):
    #global variables
    global mass
    z = state[0]
    v = state[1]

    # first derivaitve of z (veloctiy)
    dzdt = v

    #computing total forces (may change later)
    gravity = -9.81*mass
    aero = 0
    thrust = 0
    forces = gravity + aero + thrust

    #computing acceleration by + forces on the object and / by mass
    dzzdt = forces/mass

    #computing state derivative
    dstate = np.array([dzdt,dzzdt])

    return dstate
###the function must be integrated###
##initial values
z0 = 0
v0 = 100
stateinitial = np.array([z0, v0])

##Time
tout = np.linspace(0, 21, 1000)
#integration
stateout = sci.odeint(statederivative, stateinitial, tout)
zout = stateout[:,0]
vout = stateout[:,1]

#### plotting
#altitude / time
plt.figure(1)
plt.plot(tout,zout)
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Altitude-Time Graph")

#speed/time
plt.figure(2)
plt.plot(tout, vout)
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Velocity-Time Graph")
plt.show()