# Rocket Trajectory Simulator

This is a python trajectory simulator of vertical rocket flight, built to numerically and graphically model altitude and velocity over time using a flat-Earth, one-dimensional dynamics model.

## Overview

This project solves the equations of motion for a rocket moving along a single vertical axis, using `scipy.integrate.odeint` to integrate the system forward in time. This basic simulator servers as the base for a complete fuller flight simulator.

## Physics Model

The simulation treats the rocket as an object moving vertically, led by Newton's second law:

```
F = m * a
```

The state of the system at any given time is described by the following two variables:

- **z** — altitude above the surface (m)
- **v** — vertical velocity (m/s)

which gives the first-order system:

```
dz/dt = v
dv/dt = (F_gravity + F_aero + F_thrust) / m
```

**Assumptions:**
- Flat Earth 
- Constant gravitational acceleration (g = 9.81 m/s²)
- Aerodynamic drag and thrust are currently set to zero (placeholders for future work)
- Constant mass (no propellant burn modeled yet)

## Current Parameters

| Parameter | Value |
|---|---|
| Mass | 40 g |
| Initial altitude (z₀) | 0 m |
| Initial velocity (v₀) | 100 m/s |
| Simulation time | 0–21 s |
| Time steps | 1000 |

These are set as variables near the top of the script and can be edited directly to test different conditions.

## Dependencies

- `numpy`
- `matplotlib`
- `scipy`


## Usage

Run the script directly:

```bash
python trajectory_sim.py
```

This integrates the equations of motion over the set time duration and generates two plots:

**Altitude vs. Time** — tracks the rocket's height above the surface
**Velocity vs. Time** — tracks vertical speed throughout the flight

## Next Steps/Improvements

- Add aerodynamic drag as a function of velocity, air density, and drag coefficient
- Switch to a 3D Earth model
- Add the option of a two-stage rocket
- Add a thrust curve to model powered ascent
- Model mass loss as propellant burns (variable mass system)
- Extend to include an atmospheric density model 