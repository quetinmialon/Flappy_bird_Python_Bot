import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
from flappy_bird_env import FlappyBirdEnv

if __name__ == "__main__":
    env = make_vec_env(FlappyBirdEnv, n_envs=1)

    model = DQN('CnnPolicy', env, verbose=1)
    model.learn(total_timesteps=50000)

    model.save("flappybird_dqn")

    obs = env.reset()
    for i in range(1000):
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, done, info = env.step(action)
        env.render()
        if done:
            obs = env.reset()




