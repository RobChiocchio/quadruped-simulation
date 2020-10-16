from gym.envs.registration import register

register(
    id="SwolArmEnv-v0",
    entry_point="envs.swol_arm_gym_env:SwolArmEnv",
    max_episode_steps=1000,
    reward_threshold=5.0,
)