import numpy as np
import gym

from .color_style import DeepMindColor
from .object import Object
from .motion import VonNeumannMotion
from .motion import MooreMotion
from .maze import BaseMaze
from .env import BaseEnv, Maze, Env

from .generators import random_maze

env_id = "EmptyMaze-10x10-FixedGoal-v0"
x = random_maze(width=10, height=10, complexity=0.7, density=0.0)
EmptyMaze_10x10_FixedGoal_v0 = Env(Maze(x),
          randomize_start=True, 
          randomize_goal=False)
EmptyMaze_10x10_FixedGoal_v0_entry_point = lambda: EmptyMaze_10x10_FixedGoal_v0 
gym.envs.register(id=env_id, entry_point=EmptyMaze_10x10_FixedGoal_v0_entry_point, max_episode_steps=200)


env_id = "EmptyMaze-10x10-RandomGoal-v0"
x = random_maze(width=10, height=10, complexity=0.7, density=0.0)
EmptyMaze_10x10_RandomGoal_v0 = Env(Maze(x),
          randomize_start=True, 
          randomize_goal=True)
EmptyMaze_10x10_RandomGoal_v0_entry_point = lambda: EmptyMaze_10x10_RandomGoal_v0
gym.envs.register(id=env_id, entry_point=EmptyMaze_10x10_RandomGoal_v0_entry_point, max_episode_steps=200)


x10 = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

env_id = "Maze-10x10-FixedGoal-v0"
Maze_10x10_FixedGoal_v0 = Env(Maze(x10),
          randomize_start=True, 
          randomize_goal=False)
Maze_10x10_FixedGoal_v0_entry_point = lambda: Maze_10x10_FixedGoal_v0
gym.envs.register(id=env_id, entry_point=Maze_10x10_FixedGoal_v0_entry_point, max_episode_steps=200)


env_id = "Maze-10x10-RandomGoal-v0"
Maze_10x10_RandomGoal_v0 = Env(Maze(x10),
          randomize_start=True, 
          randomize_goal=True)
Maze_10x10_RandomGoal_v0_entry_point = lambda: Maze_10x10_RandomGoal_v0
gym.envs.register(id=env_id, entry_point=Maze_10x10_RandomGoal_v0_entry_point, max_episode_steps=200)


x15 = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
       [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

env_id = "Maze-15x15-FixedGoal-v0"
Maze_15x15_FixedGoal_v0 = Env(Maze(x15),
          randomize_start=True, 
          randomize_goal=False)
Maze_15x15_FixedGoal_v0_entry_point = lambda: Maze_15x15_FixedGoal_v0
gym.envs.register(id=env_id, entry_point=Maze_15x15_FixedGoal_v0_entry_point, max_episode_steps=200)


env_id = "Maze-15x15-RandomGoal-v0"
Maze_15x15_RandomGoal_v0 = Env(Maze(x15),
          randomize_start=True, 
          randomize_goal=True)
Maze_15x15_RandomGoal_v0_entry_point = lambda: Maze_15x15_RandomGoal_v0
gym.envs.register(id=env_id, entry_point=Maze_15x15_RandomGoal_v0_entry_point, max_episode_steps=200)



x25 = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
               [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
               [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
               [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
               [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
               [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

env_id = "Maze-25x25-FixedGoal-v0"
Maze_25x25_FixedGoal_v0 = Env(Maze(x25),
          randomize_start=True, 
          randomize_goal=False)
Maze_25x25_FixedGoal_v0_entry_point = lambda: Maze_25x25_FixedGoal_v0
gym.envs.register(id=env_id, entry_point=Maze_25x25_FixedGoal_v0_entry_point, max_episode_steps=300)


env_id = "Maze-25x25-RandomGoal-v0"
Maze_25x25_RandomGoal_v0 = Env(Maze(x25),
          randomize_start=True, 
          randomize_goal=True)
Maze_25x25_RandomGoal_v0_entry_point = lambda: Maze_25x25_RandomGoal_v0
gym.envs.register(id=env_id, entry_point=Maze_25x25_RandomGoal_v0_entry_point, max_episode_steps=300)



