

import numpy as np
import gym
from gym import spaces


def example_1():
    # set up the environment
    env = gym.make('MountainCar-v0')

    env.reset()

    for _ in range(500):

        env.render()

        # take a random action
        env.step(env.action_space.sample())

        # step function returns 4 values
        # observation(object) | reward(float) | done(boolean) | info(dict)


    env.close()

def example_2():

    env = gym.make('CartPole-v0')

    for i_episode in range(20):
        observation = env.reset()

        for t in range(100):

            env.render()
            print(observation)

            action = env.action_space.sample()

            observation, reward, done, info = env.step(action)

            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break
    env.close()

def example_3():

    env = gym.make('CartPole-v0')

    print(env.action_space)

    print(env.observation_space)

    print(env.observation_space.low)

    print(env.observation_space.high)

def example_4():

    space = spaces.Discrete(8)

    x = space.sample()

    assert space.contains(x)

    assert space.n == 8

def example_5():

    print(gym.envs.registry.all())

