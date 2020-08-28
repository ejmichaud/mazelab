import numpy as np
import gym

from .color_style import DeepMindColor
from .object import Object
from .motion import VonNeumannMotion, MichaudMotion
from .motion import MooreMotion
from .maze import BaseMaze
from .env import (
        Maze,
        MazeEnv,
        RandomizingMazeEnv,
        NonTerminatingMazeEnv,
        RandomizingNonTerminatingMazeEnv
)
from .generators import random_maze

env_id = "EmptyMaze-10x10-FixedGoal-v2"
x = random_maze(width=10, height=10, complexity=0.7, density=0.0)
EmptyMaze_10x10_FixedGoal_v2 = MazeEnv(Maze(x),
          randomize_start=True, 
          randomize_goal=False)
EmptyMaze_10x10_FixedGoal_v2_entry_point = lambda: EmptyMaze_10x10_FixedGoal_v2 
gym.envs.register(id=env_id, entry_point=EmptyMaze_10x10_FixedGoal_v2_entry_point, max_episode_steps=200)


env_id = "EmptyMaze-10x10-FixedGoal-NonTerminating-v2"
x = random_maze(width=10, height=10, complexity=0.7, density=0.0)
EmptyMaze_10x10_FixedGoal_NonTerminating_v2 = NonTerminatingMazeEnv(Maze(x),
          randomize_start=True, 
          randomize_goal=False)
EmptyMaze_10x10_FixedGoal_NonTerminating_v2_entry_point = lambda: EmptyMaze_10x10_FixedGoal_NonTerminating_v2 
gym.envs.register(id=env_id, entry_point=EmptyMaze_10x10_FixedGoal_NonTerminating_v2_entry_point, max_episode_steps=50)


env_id = "EmptyMaze-10x10-CoinFlipGoal-v2"
x = random_maze(width=10, height=10, complexity=0.7, density=0.0)
EmptyMaze_10x10_CoinFlipGoal_v2 = MazeEnv(Maze(x),
          randomize_start=True, 
          randomize_goal=False,
          coinflip_goal=True)
EmptyMaze_10x10_CoinFlipGoal_v2_entry_point = lambda: EmptyMaze_10x10_CoinFlipGoal_v2 
gym.envs.register(id=env_id, entry_point=EmptyMaze_10x10_CoinFlipGoal_v2_entry_point, max_episode_steps=200)


env_id = "EmptyMaze-10x10-CoinFlipGoal-NonTerminating-v2"
x = random_maze(width=10, height=10, complexity=0.7, density=0.0)
EmptyMaze_10x10_CoinFlipGoal_NonTerminating_v2 = NonTerminatingMazeEnv(Maze(x),
          randomize_start=True, 
          randomize_goal=False,
          coinflip_goal=True)
EmptyMaze_10x10_CoinFlipGoal_NonTerminating_v2_entry_point = lambda: EmptyMaze_10x10_CoinFlipGoal_NonTerminating_v2
gym.envs.register(id=env_id, entry_point=EmptyMaze_10x10_CoinFlipGoal_NonTerminating_v2_entry_point, max_episode_steps=50)


env_id = "EmptyMaze-10x10-RandomGoal-v2"
x = random_maze(width=10, height=10, complexity=0.7, density=0.0)
EmptyMaze_10x10_RandomGoal_v2 = MazeEnv(Maze(x),
          randomize_start=True, 
          randomize_goal=True)
EmptyMaze_10x10_RandomGoal_v2_entry_point = lambda: EmptyMaze_10x10_RandomGoal_v2
gym.envs.register(id=env_id, entry_point=EmptyMaze_10x10_RandomGoal_v2_entry_point, max_episode_steps=200)


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

env_id = "Maze-10x10-FixedGoal-v2"
Maze_10x10_FixedGoal_v2 = MazeEnv(Maze(x10),
          randomize_start=True, 
          randomize_goal=False)
Maze_10x10_FixedGoal_v2_entry_point = lambda: Maze_10x10_FixedGoal_v2
gym.envs.register(id=env_id, entry_point=Maze_10x10_FixedGoal_v2_entry_point, max_episode_steps=200)

env_id = "Maze-10x10-FixedGoal-NonTerminating-v2"
Maze_10x10_FixedGoal_NonTerminating_v2 = NonTerminatingMazeEnv(Maze(x10),
          randomize_start=True, 
          randomize_goal=False)
Maze_10x10_FixedGoal_NonTerminating_v2_entry_point = lambda: Maze_10x10_FixedGoal_NonTerminating_v2
gym.envs.register(id=env_id, entry_point=Maze_10x10_FixedGoal_NonTerminating_v2_entry_point, max_episode_steps=50)


env_id = "Maze-10x10-RandomGoal-v2"
Maze_10x10_RandomGoal_v2 = MazeEnv(Maze(x10),
          randomize_start=True, 
          randomize_goal=True)
Maze_10x10_RandomGoal_v2_entry_point = lambda: Maze_10x10_RandomGoal_v2
gym.envs.register(id=env_id, entry_point=Maze_10x10_RandomGoal_v2_entry_point, max_episode_steps=200)


env_id = "Maze-10x10-CoinFlipGoal-NonTerminating-v2"
Maze_10x10_CoinFlipGoal_NonTerminating_v2 = NonTerminatingMazeEnv(Maze(x10),
          randomize_start=True, 
          randomize_goal=False,
          coinflip_goal=True)
Maze_10x10_CoinFlipGoal_NonTerminating_v2_entry_point = lambda: Maze_10x10_CoinFlipGoal_NonTerminating_v2
gym.envs.register(id=env_id, entry_point=Maze_10x10_CoinFlipGoal_NonTerminating_v2_entry_point, max_episode_steps=100)




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

env_id = "Maze-15x15-FixedGoal-v2"
Maze_15x15_FixedGoal_v2 = MazeEnv(Maze(x15),
          randomize_start=True, 
          randomize_goal=False)
Maze_15x15_FixedGoal_v2_entry_point = lambda: Maze_15x15_FixedGoal_v2
gym.envs.register(id=env_id, entry_point=Maze_15x15_FixedGoal_v2_entry_point, max_episode_steps=200)


env_id = "Maze-15x15-FixedGoal-NonTerminating-v2"
Maze_15x15_FixedGoal_NonTerminating_v2 = NonTerminatingMazeEnv(Maze(x15),
          randomize_start=True, 
          randomize_goal=False)
Maze_15x15_FixedGoal_NonTerminating_v2_entry_point = lambda: Maze_15x15_FixedGoal_NonTerminating_v2
gym.envs.register(id=env_id, entry_point=Maze_15x15_FixedGoal_NonTerminating_v2_entry_point, max_episode_steps=100)


env_id = "Maze-15x15-RandomGoal-v2"
Maze_15x15_RandomGoal_v2 = MazeEnv(Maze(x15),
          randomize_start=True, 
          randomize_goal=True)
Maze_15x15_RandomGoal_v2_entry_point = lambda: Maze_15x15_RandomGoal_v2
gym.envs.register(id=env_id, entry_point=Maze_15x15_RandomGoal_v2_entry_point, max_episode_steps=200)


env_id = "Maze-15x15-CoinFlipGoal-NonTerminating-v2"
Maze_15x15_CoinFlipGoal_NonTerminating_v2 = NonTerminatingMazeEnv(Maze(x15),
          randomize_start=True, 
          randomize_goal=False,
          coinflip_goal=True)
Maze_15x15_CoinFlipGoal_NonTerminating_v2_entry_point = lambda: Maze_15x15_CoinFlipGoal_NonTerminating_v2
gym.envs.register(id=env_id, entry_point=Maze_15x15_CoinFlipGoal_NonTerminating_v2_entry_point, max_episode_steps=100)


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

env_id = "Maze-25x25-FixedGoal-v2"
Maze_25x25_FixedGoal_v2 = MazeEnv(Maze(x25),
          randomize_start=True, 
          randomize_goal=False)
Maze_25x25_FixedGoal_v2_entry_point = lambda: Maze_25x25_FixedGoal_v2
gym.envs.register(id=env_id, entry_point=Maze_25x25_FixedGoal_v2_entry_point, max_episode_steps=300)


env_id = "Maze-25x25-RandomGoal-v2"
Maze_25x25_RandomGoal_v2 = MazeEnv(Maze(x25),
          randomize_start=True, 
          randomize_goal=True)
Maze_25x25_RandomGoal_v2_entry_point = lambda: Maze_25x25_RandomGoal_v2
gym.envs.register(id=env_id, entry_point=Maze_25x25_RandomGoal_v2_entry_point, max_episode_steps=300)


env_id = "RandomMaze-7x7-FixedGoal-v2"
RandomMaze_7x7_FixedGoal_v2 = RandomizingMazeEnv(
    width=7,
    height=7,
    randomize_start=True,
    randomize_goal=False
)
RandomMaze_7x7_FixedGoal_v2_entry_point = lambda: RandomMaze_7x7_FixedGoal_v2
gym.envs.register(id=env_id, entry_point=RandomMaze_7x7_FixedGoal_v2_entry_point, max_episode_steps=300)


env_id = "RandomMaze-7x7-FixedGoal-NonTerminating-v2"
RandomMaze_7x7_FixedGoal_NonTerminating_v2 = RandomizingNonTerminatingMazeEnv(
    width=7,
    height=7,
    randomize_start=True,
    randomize_goal=False
)
RandomMaze_7x7_FixedGoal_NonTerminating_v2_entry_point = lambda: RandomMaze_7x7_FixedGoal_NonTerminating_v2
gym.envs.register(id=env_id, entry_point=RandomMaze_7x7_FixedGoal_NonTerminating_v2_entry_point, max_episode_steps=50)


env_id = "RandomMaze-7x7-RandomGoal-v2"
RandomMaze_7x7_RandomGoal_v2 = RandomizingMazeEnv(
    width=7,
    height=7,
    randomize_start=True,
    randomize_goal=True
)
RandomMaze_7x7_RandomGoal_v2_entry_point = lambda: RandomMaze_7x7_RandomGoal_v2
gym.envs.register(id=env_id, entry_point=RandomMaze_7x7_RandomGoal_v2_entry_point, max_episode_steps=300)


env_id = "RandomMaze-7x7-CoinFlipGoal-NonTerminating-v2"
RandomMaze_7x7_CoinFlipGoal_NonTerminating_v2 = RandomizingNonTerminatingMazeEnv(
    width=7,
    height=7,
    randomize_start=True,
    randomize_goal=False,
    coinflip_goal=True
)
RandomMaze_7x7_CoinFlipGoal_NonTerminating_v2_entry_point = lambda: RandomMaze_7x7_CoinFlipGoal_NonTerminating_v2
gym.envs.register(id=env_id, entry_point=RandomMaze_7x7_CoinFlipGoal_NonTerminating_v2_entry_point, max_episode_steps=50)


env_id = "RandomMaze-8x8-FixedGoal-v2"
RandomMaze_8x8_FixedGoal_v2 = RandomizingMazeEnv(
    width=8,
    height=8,
    randomize_start=True,
    randomize_goal=False
)
RandomMaze_8x8_FixedGoal_v2_entry_point = lambda: RandomMaze_8x8_FixedGoal_v2
gym.envs.register(id=env_id, entry_point=RandomMaze_8x8_FixedGoal_v2_entry_point, max_episode_steps=300)

env_id = "RandomMaze-8x8-FixedGoal-NonTerminating-v2"
RandomMaze_8x8_FixedGoal_NonTerminating_v2 = RandomizingNonTerminatingMazeEnv(
    width=8,
    height=8,
    randomize_start=True,
    randomize_goal=False
)
RandomMaze_8x8_FixedGoal_NonTerminating_v2_entry_point = lambda: RandomMaze_8x8_FixedGoal_NonTerminating_v2
gym.envs.register(id=env_id, entry_point=RandomMaze_8x8_FixedGoal_NonTerminating_v2_entry_point, max_episode_steps=50)


env_id = "RandomMaze-8x8-RandomGoal-v2"
RandomMaze_8x8_RandomGoal_v2 = RandomizingMazeEnv(
    width=8,
    height=8,
    randomize_start=True,
    randomize_goal=True
)
RandomMaze_8x8_RandomGoal_v2_entry_point = lambda: RandomMaze_8x8_RandomGoal_v2
gym.envs.register(id=env_id, entry_point=RandomMaze_8x8_RandomGoal_v2_entry_point, max_episode_steps=300)


env_id = "RandomMaze-8x8-CoinFlipGoal-v2"
RandomMaze_8x8_CoinFlipGoal_v2 = RandomizingMazeEnv(
    width=8,
    height=8,
    randomize_start=True,
    randomize_goal=False,
    coinflip_goal=True
)
RandomMaze_8x8_CoinFlipGoal_v2_entry_point = lambda: RandomMaze_8x8_CoinFlipGoal_v2
gym.envs.register(id=env_id, entry_point=RandomMaze_8x8_CoinFlipGoal_v2_entry_point, max_episode_steps=300)


env_id = "RandomMaze-8x8-CoinFlipGoal-NonTerminating-v2"
RandomMaze_8x8_CoinFlipGoal_NonTerminating_v2 = RandomizingNonTerminatingMazeEnv(
    width=8,
    height=8,
    randomize_start=True,
    randomize_goal=False,
    coinflip_goal=True
)
RandomMaze_8x8_CoinFlipGoal_NonTerminating_v2_entry_point = lambda: RandomMaze_8x8_CoinFlipGoal_NonTerminating_v2
gym.envs.register(id=env_id, entry_point=RandomMaze_8x8_CoinFlipGoal_NonTerminating_v2_entry_point, max_episode_steps=50)


