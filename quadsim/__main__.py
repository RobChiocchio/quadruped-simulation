import os
import sys
import time

import numpy as np
import pybullet as p
import pybullet_data

from quadsim.envs.swol_kat_gym_env import SwolKatEnv

if __name__ == "__main__":
    env = SwolKatEnv(render=True)
    env.render(mode="human")

    dof = env._pybullet_client.getNumJoints(env.minitaur.quadruped)

    sliders = []
    
    for j in range(dof):
        joint_info = env._pybullet_client.getJointInfo(env.minitaur.quadruped, j)
        print(joint_info)
        if (joint_info[2] != 4): # and (joint_info[16] != -1)
            sliders.append(env._pybullet_client.addUserDebugParameter(f"{j} - {joint_info[1]}", -np.pi/2, np.pi/2, 0))
            #p.setJointMotorControl2(robot, j, p.VELOCITY_CONTROL, force=0)
            #env._pybullet_client.resetJointState(env.minitaur.quadruped, j, joint_positions[j])  
            #env._pybullet_client.setJointMotorControl(env.minitaur.quadruped, j, env._pybullet_client.POSITION_CONTROL, joint_positions[j])

    joint_positions = [0]*len(sliders)

    while True:
        for j in range(len(sliders)):
            joint_positions[j] = env._pybullet_client.readUserDebugParameter(sliders[j])
            #env._pybullet_client.setJointMotorControl(env.minitaur.quadruped, j, p.POSITION_CONTROL, joint_positions[j])

        env.step(joint_positions)
        env.render(mode='human')
        env._is_render = True # DEBUG
        dt = 1. / 240.
        time.sleep(dt)

    #p.disconnect()
    env.close()
    sys.exit(0)