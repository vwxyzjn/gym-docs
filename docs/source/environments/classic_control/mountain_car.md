---
AUTOGENERATED: DO NOT EDIT FILE DIRECTLY
title: Mountain Car
---

# Mountain Car

```{figure} ../../_static/videos/classic_control/mountain_car.gif 
:width: 200px
:name: mountain_car
```

This environment is part of the <a href='..'>Classic Control environments</a>. Please read that page first for general information.

|   |   |
|---|---|
| Action Space | Discrete(3) |
| Observation Shape | (2,) |
| Observation High | [0.6  0.07] |
| Observation Low | [-1.2  -0.07] |
| Import | `gym.make("MountainCar-v0")` | 


### Description

The Mountain Car MDP is a deterministic MDP that consists of a car placed stochastically
at the bottom of a sinusoidal valley, with the only possible actions being the accelerations
that can be applied to the car in either direction. The goal of the MDP is to strategically
accelerate the car to reach the goal state on top of the right hill. There are two versions
of the mountain car domain in gym: one with discrete actions and one with continuous.
This version is the one with discrete actions.

This MDP first appeared in [Andrew Moore's PhD Thesis (1990)](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-209.pdf)

```
@TECHREPORT{Moore90efficientmemory-based,
    author = {Andrew William Moore},
    title = {Efficient Memory-based Learning for Robot Control},
    institution = {University of Cambridge},
    year = {1990}
}
```

### Observation Space

The observation is a `ndarray` with shape `(2,)` where the elements correspond to the following:

| Num | Observation                                                 | Min                | Max    | Unit |
|-----|-------------------------------------------------------------|--------------------|--------|------|
| 0   | position of the car along the x-axis                        | -Inf               | Inf    | position (m) |
| 1   | velocity of the car                                         | -Inf               | Inf  | position (m) |

### Action Space

There are 3 discrete deterministic actions:

| Num | Observation                                                 | Value   | Unit |
|-----|-------------------------------------------------------------|---------|------|
| 0   | Accelerate to the left                                      | Inf    | position (m) |
| 1   | Don't accelerate                                            | Inf  | position (m) |
| 2   | Accelerate to the right                                     | Inf    | position (m) |

### Transition Dynamics:

Given an action, the mountain car follows the following transition dynamics:

*velocity<sub>t+1</sub> = velocity<sub>t</sub> + (action - 1) * force - cos(3 * position<sub>t</sub>) * gravity*

*position<sub>t+1</sub> = position<sub>t</sub> + velocity<sub>t+1</sub>*

where force = 0.001 and gravity = 0.0025. The collisions at either end are inelastic with the velocity set to 0 upon collision with the wall. The position is clipped to the range `[-1.2, 0.6]` and velocity is clipped to the range `[-0.07, 0.07]`.


### Reward:

The goal is to reach the flag placed on top of the right hill as quickly as possible, as such the agent is penalised with a reward of -1 for each timestep it isn't at the goal and is not penalised (reward = 0) for when it reaches the goal.

### Starting State

The position of the car is assigned a uniform random value in *[-0.6 , -0.4]*. The starting velocity of the car is always assigned to 0.

### Episode Termination

The episode terminates if either of the following happens:
1. The position of the car is greater than or equal to 0.5 (the goal position on top of the right hill)
2. The length of the episode is 200.


### Arguments

```
gym.make('MountainCar-v0')
```

### Version History

* v0: Initial versions release (1.0.0)
