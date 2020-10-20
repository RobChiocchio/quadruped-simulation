import os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
os.sys.path.insert(0, parentdir)

import gym
import numpy as np

from envs.swol_arm_gym_env import SwolArmEnv

from stable_baselines import SAC
from stable_baselines.common.env_checker import check_env

env_id = "SwolArmEnv-v0"
num_cpu = 4

# env = gym.make("KukaBulletEnv-v0")
env = SwolArmEnv(renders=True)
check_env(env, skip_render_check=False)

model = SAC.load("sac_swol_arm")
print(model)

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
