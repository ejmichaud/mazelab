from gym.envs.registration import registry, register, make, spec

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



##### EmptyMaze-10x10 variants #####
for goal_config in ['FixedGoal', 'CoinFlipGoal', 'TwoGoals', 'RandomGoal']:
    x = random_maze(width=10, height=10, complexity=0.7, density=0)
    register(
        id = "EmptyMaze-10x10-{}-v3".format(goal_config),
        entry_point = 'mazelab.env:MazeEnv',
        max_episode_steps = 200,
        kwargs={
            'maze': Maze(x),
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal'),
            'two_goals': (goal_config == 'TwoGoals'),
        }
    )
    register(
        id = "EmptyMaze-10x10-{}-NonTerminating-v3".format(goal_config),
        entry_point = 'mazelab.env:NonTerminatingMazeEnv',
        max_episode_steps = 50,
        kwargs={
            'maze': Maze(x),
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal'),
            'two_goals': (goal_config == 'TwoGoals'),
        }
    )

##### Maze-10x10 variants #####
for goal_config in ['FixedGoal', 'CoinFlipGoal', 'TwoGoals', 'RandomGoal']:
    register(
        id = "Maze-10x10-{}-v3".format(goal_config),
        entry_point = 'mazelab.env:MazeEnv',
        max_episode_steps = 200,
        kwargs={
            'maze': Maze(x10),
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal'),
            'two_goals': (goal_config == 'TwoGoals'),
        }
    )
    register(
        id = "Maze-10x10-{}-NonTerminating-v3".format(goal_config),
        entry_point = 'mazelab.env:NonTerminatingMazeEnv',
        max_episode_steps = 50,
        kwargs={
            'maze': Maze(x10),
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal'),
            'two_goals': (goal_config == 'TwoGoals'),
        }
    )

##### Maze-15x15 variants #####
for goal_config in ['FixedGoal', 'CoinFlipGoal', 'TwoGoals', 'RandomGoal']:
    register(
        id = "Maze-15x15-{}-v3".format(goal_config),
        entry_point = 'mazelab.env:MazeEnv',
        max_episode_steps = 200,
        kwargs={
            'maze': Maze(x15),
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal'),
            'two_goals': (goal_config == 'TwoGoals'),
        }
    )
    register(
        id = "Maze-15x15-{}-NonTerminating-v3".format(goal_config),
        entry_point = 'mazelab.env:NonTerminatingMazeEnv',
        max_episode_steps = 50,
        kwargs={
            'maze': Maze(x15),
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal'),
            'two_goals': (goal_config == 'TwoGoals'),
        }
    )

##### Maze-25x25 variants #####
for goal_config in ['FixedGoal', 'CoinFlipGoal', 'TwoGoals', 'RandomGoal']:
    register(
        id = "Maze-25x25-{}-v3".format(goal_config),
        entry_point = 'mazelab.env:MazeEnv',
        max_episode_steps = 200,
        kwargs={
            'maze': Maze(x25),
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal'),
            'two_goals': (goal_config == 'TwoGoals'),
        }
    )
    register(
        id = "Maze-25x25-{}-NonTerminating-v3".format(goal_config),
        entry_point = 'mazelab.env:NonTerminatingMazeEnv',
        max_episode_steps = 50,
        kwargs={
            'maze': Maze(x25),
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal'),
            'two_goals': (goal_config == 'TwoGoals'),
        }
    )

##### RandomMaze-7x7 variants #####
for goal_config in ['FixedGoal', 'CoinFlipGoal', 'RandomGoal']:
    register(
        id = "RandomMaze-7x7-{}-v3".format(goal_config),
        entry_point = 'mazelab.env:RandomizingMazeEnv',
        max_episode_steps = 200,
        kwargs={
            'width': 7,
            'height': 7,
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal')
        }
    )
    register(
        id = "RandomMaze-7x7-{}-NonTerminating-v3".format(goal_config),
        entry_point = 'mazelab.env:RandomizingNonTerminatingMazeEnv',
        max_episode_steps = 50,
        kwargs={
            'width': 7,
            'height': 7,
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal')
        }
    )

##### RandomMaze-8x8 variants #####
for goal_config in ['FixedGoal', 'CoinFlipGoal', 'RandomGoal']:
    register(
        id = "RandomMaze-8x8-{}-v3".format(goal_config),
        entry_point = 'mazelab.env:RandomizingMazeEnv',
        max_episode_steps = 200,
        kwargs={
            'width': 8,
            'height': 8,
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal')
        }
    )
    register(
        id = "RandomMaze-8x8-{}-NonTerminating-v3".format(goal_config),
        entry_point = 'mazelab.env:RandomizingNonTerminatingMazeEnv',
        max_episode_steps = 50,
        kwargs={
            'width': 8,
            'height': 8,
            'randomize_start': True,
            'randomize_goal': (goal_config == 'RandomGoal'),
            'coinflip_goal': (goal_config == 'CoinFlipGoal')
        }
    )


