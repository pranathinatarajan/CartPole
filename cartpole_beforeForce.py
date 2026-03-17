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
while True:
    py.stepSimulation()
    time.sleep(1/240)