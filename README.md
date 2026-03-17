**Cart-Pole Stabilization - a simple pybullet simulation**

- This is a simple simulation of an inverted pendulum on a moving cart built entirely in PyBullet. A PD controller is used to stabilize a pole sitting atop the cart and prevent it from falling down, until the cart reaches the end of the rail using appropriate forces.

- **cartpole_beforeForce.py** aims to show the simulation of the cartpole system before the required force is applied. In this scenario, the pole falls almost immediately due to the initial disturbance. 

- **cartpole_afterForce.py** displays the required force being applied on the cartpole, and how the pole is able to remain upright till the end of the rail.

- **modified_cartpole.urdf** contains the modified cartpole's joints and links.

**Note: the values of Kd and Kp were chosen arbitrarily** 

**Relevance**
- Built to understand the physical development of a cart-pole system as well as validate the model prior to being built using simulation. 
