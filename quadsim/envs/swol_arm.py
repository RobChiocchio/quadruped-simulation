import pybullet as p
from envs.swol_robot import SwolRobot

class SwolArm(SwolRobot):
    def __init__(self, basePosition=[0, 0, 0], baseOrientation=[0, 0, 0, 1]):
        model_urdf = "doggo-arm.urdf"
        robot_name = "arm"
        action_dim = 0
        obs_dim = 0
        fixed_base = True
        self_collision=False
        SwolRobot.__init__(self, model_urdf, robot_name, action_dim, obs_dim, basePosition, baseOrientation, fixed_base, self_collision)
