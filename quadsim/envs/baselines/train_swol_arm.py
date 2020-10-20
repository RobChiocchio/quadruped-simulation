import os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
os.sys.path.insert(0, parentdir)

import gym
import numpy as np

from envs.swol_arm_gym_env import SwolArmEnv

from stable_baselines.sac.policies import MlpPolicy
from stable_baselines import SAC

# from stable_baselines.common.vec_env import SubprocVecEnv
# from stable_baselines.common import set_global_seeds, make_vec_env
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.evaluation import evaluate_policy

# env = gym.make("SwolArmEnv-v0")
env_id = "SwolArmEnv-v0"
num_cpu = 4

# env = SubprocVecEnv([make_env(env_id, i) for i in range])
env = gym.make(env_id)

check_env(env, skip_render_check=True)

model = SAC(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=100000)

model.save("sac_swol_arm")
# env.save()
