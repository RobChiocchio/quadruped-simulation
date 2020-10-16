import pybullet as p
from pybullet_envs.gym_locomotion_envs import WalkerBaseBulletEnv
from envs.swol_arm import SwolArm

class SwolArmEnv(WalkerBaseBulletEnv):
    def __init__(self, render=False):
        self.robot = SwolArm()
        WalkerBaseBulletEnv.__init__(self, self.robot, render)
