import os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
os.sys.path.insert(0, parentdir)

import gym
import numpy as np

from envs.swol_arm_gym_env import SwolArmEnv

from stable_baselines.sac.policies import MlpPolicy
from stable_baselines import SAC

from stable_baselines.common.env_checker import check_env

env = gym.make("SwolArmEnv-v0")

check_env(env, skip_render_check=False)

model = SAC(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=100000)