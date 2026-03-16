import pybullet as py
import math 
import pybullet_data

#setting up pybullet
py.connect(direct)
py.resetSimulation()
py.setAdditionalSearchPath(pybullet_data.getDataPath())
py.setGravity(0,0,-9.8)

#Loading the plane and the cartpole
py.loadURDF("plane.urdf", [0,0,0], [0,0,0,1])
cartpole = py.loadURDF("cartpole.urdf", [0,0,0.1], [0,0,0,1])

