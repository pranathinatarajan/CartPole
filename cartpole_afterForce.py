import pybullet as py
import time 
import pybullet_data

#setting up pybullet
py.connect(py.GUI)
py.resetSimulation()
py.setAdditionalSearchPath(pybullet_data.getDataPath())
py.setGravity(0,0,-9.8)

#Loading the plane and the cartpole
py.loadURDF("plane.urdf", [0,0,0], [0,0,0,1])
cartpole = py.loadURDF("modified_cartpole.urdf", [0,0,0.1], [0,0,0,1])

#Printing joint info
cartpole_position = py.getBasePositionAndOrientation(cartpole)
for i in range (py.getNumJoints(cartpole)):
    joint_info = py.getJointInfo(cartpole, i)
    print(f"Joint = {i}, Name = {joint_info[1]}, Type = {joint_info[2]}")
Rail = 1
Pole = 2

#Giving the pole a small push to destabilize 
py.resetJointState(cartpole, Pole, targetValue = 0.05 )

#Additional change to friction to allow free movement
py.setJointMotorControl2(cartpole, Rail, controlMode = py.VELOCITY_CONTROL, force = 0)
py.setJointMotorControl2(cartpole, Pole, controlMode = py.VELOCITY_CONTROL, force = 0)

#main loop

#Assigning Kp and Kd 
Kp = 40
Kd = 10

while True:
    #Examining the state of the pole and rail
    pole_state = py.getJointState(cartpole, Pole)
    pole_angle = pole_state[0]
    pole_AngVelocity = pole_state[1]
    
    rail_state = py.getJointState(cartpole, Rail)
    rail_angle = rail_state[0]
    rail_AngVelocity = rail_state[1]

    #Computing the force required using known formula
    force = pole_angle*Kp + pole_AngVelocity*Kd
    print(f"Force = {force}")

    #Applying the force to the rail
    py.setJointMotorControl2(cartpole, Rail, controlMode = py.TORQUE_CONTROL, force = force)

    py.stepSimulation()
    time.sleep(1/240)