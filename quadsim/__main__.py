import os
import sys

import glfw
import mujoco_py
import numpy as np

mj_path, _ = mujoco_py.utils.discover_mujoco()
model = mujoco_py.load_model_from_path("quadruped.xml")
sim = mujoco_py.MjSim(model)
viewer = mujoco_py.MjViewer(sim)

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


def key_callback(window, key, scancode, action, mods):
    if action != glfw.RELEASE:
        return
    elif key == glfw.KEY_HOME:
        sim.reset()
        set_action(sim, actions["stand"])
    elif key == glfw.KEY_0:
        set_action(sim, actions["stand"])
    elif key == glfw.KEY_MINUS:
        set_action(sim, actions["step_lfrr"])
    elif key == glfw.KEY_EQUAL:
        set_action(sim, actions["step_rflr"])
    elif key == glfw.KEY_9:
        set_action(sim, actions["crouch"])
    elif key == glfw.KEY_8:
        set_action(sim, actions["straight"])
    else:
        viewer.key_callback(window, key, scancode, action, mods)


glfw.set_key_callback(viewer.window, key_callback)

# sim.data.ctrl[0] = np.deg2rad(30) # fl_hip
# sim.data.ctrl[1] = np.deg2rad(-60) # fl_knee
# sim.data.ctrl[2] = np.deg2rad(-30) # fl_ankle

# sim.data.ctrl[3] = np.deg2rad(30) # fr_hip
# sim.data.ctrl[4] = np.deg2rad(-60) # fr_knee
# sim.data.ctrl[5] = np.deg2rad(-30) # fr_ankle

# sim.data.ctrl[6] = np.deg2rad(30) # rl_hip
# sim.data.ctrl[7] = np.deg2rad(-60) # rl_knee
# sim.data.ctrl[8] = np.deg2rad(-30) # rl_ankle

# sim.data.ctrl[9] = np.deg2rad(30) # rr_hip
# sim.data.ctrl[10] = np.deg2rad(-60) # rr_knee
# sim.data.ctrl[11] = np.deg2rad(-30) # rr_ankle

set_action(sim, actions["stand"])

while True:
    sim.step()
    # sim.forward()
    viewer.render()
