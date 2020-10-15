import os
import sys
import time

from klampt import *
from klampt import vis
from klampt.vis.glrobotprogram import GLSimulationPlugin
import numpy as np

actions = {
    "stand": [30, -60, -30, 30, -60, -30, 30, -60, -30, 30, -60, -30],
    "step_lfrr": [45, -90, -15, 30, -60, -45, 30, -60, -45, 45, -90, -15],
    "step_rflr": [30, -60, -45, 45, -90, -15, 45, -90, -15, 30, -60, -45],
    "crouch": [60, -120, -45, 60, -120, -45, 60, -120, -45, 60, -120, -45],
    "straight": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}


def set_action(sim, action):
    if sim.data.ctrl is not None:
        for i in range(len(action)):
            sim.data.ctrl[i] = np.deg2rad(action[i])

#set_action(sim, actions["stand"])

if __name__ == "__main__":
    urdf_path = os.path.abspath("doggo-arm/urdf/doggo-arm.urdf")

    world = WorldModel()

    if os.path.exists(urdf_path):
        world.loadRobot(urdf_path)
        #controller = sim.getController()

    sim = Simulator(world)
    vis.add("world", world)
    
    viewer = GLSimulationPlugin(world)

    vis.run(viewer)

    sys.exit(0)