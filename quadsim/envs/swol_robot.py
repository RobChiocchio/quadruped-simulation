import os
import numpy as np
import pybullet as p
from pybullet_envs.robot_bases import *

class SwolRobot(URDFBasedRobot):
    def __init__(self,
                model_urdf,
                robot_name,
                action_dim,
                obs_dim,
                basePosition=[0, 0, 0],
                baseOrientation=[0, 0, 0, 1],
                fixed_base=False,
                self_collision=False):
        self.urdf_path = os.path.abspath("urdfs/doggo-arm/urdf/")
        URDFBasedRobot.__init__(self, model_urdf, robot_name, action_dim, obs_dim, basePosition, baseOrientation, fixed_base, self_collision)

    def reset(self, bullet_client):
        self._p = bullet_client
        self.ordered_joints = []

        print(os.path.join(os.path.dirname(__file__), "data", self.model_urdf))

        if self.self_collision:
            self.parts, self.jdict, self.ordered_joints, self.robot_body = self.addToScene(self._p,
                self._p.loadURDF(os.path.join(self.urdf_path, self.model_urdf),
                    basePosition=self.basePosition,
                    baseOrientation=self.baseOrientation,
                    useFixedBase=self.fixed_base,
                    flags=pybullet.URDF_USE_SELF_COLLISION | pybullet.URDF_GOOGLEY_UNDEFINED_COLORS))
        else:
            self.parts, self.jdict, self.ordered_joints, self.robot_body = self.addToScene(self._p,
                self._p.loadURDF(os.path.join(self.urdf_path, self.model_urdf),
                    basePosition=self.basePosition,
                    baseOrientation=self.baseOrientation,
                    useFixedBase=self.fixed_base, flags = pybullet.URDF_GOOGLEY_UNDEFINED_COLORS))

        self.robot_specific_reset(self._p)

        s = self.calc_state()
        self.potential = self.calc_potential()

        return s
