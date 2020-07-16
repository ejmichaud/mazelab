from abc import ABC
from abc import abstractmethod

import random

import numpy as np
import gym
from gym.utils import seeding
from gym.spaces import Box
from gym.spaces import Discrete
from PIL import Image

from mazelab import BaseMaze
from mazelab import Object
from mazelab import DeepMindColor as color
from mazelab import VonNeumannMotion

# GAMMA = 0.999

# def manhattan_distance(x, y):
#     return np.abs(x[0]-y[0]) + np.abs(x[1]-y[1])


class BaseEnv(gym.Env, ABC):
    metadata = {'render.modes': ['human', 'rgb_array'],
                'video.frames_per_second' : 3}
    reward_range = (-float('inf'), float('inf'))
    
    def __init__(self):
        self.viewer = None
        self.seed()
    
    @abstractmethod
    def step(self, action):
        pass
    
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def get_image(self):
        pass
    
    def render(self, mode='human', max_width=300):
        img = self.get_image()
        img = np.asarray(img).astype(np.uint8)
        img_height, img_width = img.shape[:2]
        ratio = max_width/img_width
        img = Image.fromarray(img).resize([int(ratio*img_width), int(ratio*img_height)])
        img = np.asarray(img)
        if mode == 'rgb_array':
            return img
        elif mode == 'human':
            from gym.envs.classic_control.rendering import SimpleImageViewer
            if self.viewer is None:
                self.viewer = SimpleImageViewer()
            self.viewer.imshow(img)
            
            return self.viewer.isopen
            
    def close(self):
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None


class Maze(BaseMaze):
    def __init__(self, maze):
        self.x = maze
        super().__init__()
    
    @property
    def size(self):
        return self.x.shape
    
    def make_objects(self):
        free = Object('free', 0, color.free, False, np.stack(np.where(self.x == 0), axis=1))
        obstacle = Object('obstacle', 1, color.obstacle, True, np.stack(np.where(self.x == 1), axis=1))
        agent = Object('agent', 2, color.agent, False, [])
        goal = Object('goal', 3, color.goal, False, [])
        return free, obstacle, agent, goal


class Env(BaseEnv):
    def __init__(self, maze, start_pos=None, 
                             goal_pos=None, 
                             randomize_start=False, 
                             randomize_goal=False,
                             # shaping=False):
                             ):
        """
        A maze gym environment based on `maze`.
        
        Args:
            maze (Maze): A maze object with "free", "obstacle", "agent", and "goal" objects.
            start_pos (tuple): If `randomize_start` is False, the agent starting position.
            goal_pos (tuple): If `randomize_goal` is False, the goal position.
            randomize_start (bool): Whether to start the agent in a random free space on reset.
            randomize_goal (bool): Whether to randomize the goal position between episodes.
        """
        super().__init__()
        self.maze = maze
        self.motions = VonNeumannMotion()
        w, h = self.maze.size
        if start_pos is None: self.start_pos = [1, 1]
        else:                 self.start_pos = start_pos
        if goal_pos is None:  self.goal_pos = [w-2, h-2]
        else:                 self.goal_pos = goal_pos
        self.randomize_start = randomize_start
        self.randomize_goal = randomize_goal
        # self.shaping = shaping
        self.observation_space = Box(low=0, high=len(self.maze.objects), shape=self.maze.size, dtype=np.uint8)
        self.action_space = Discrete(len(self.motions))
        self.reset()
        
    def step(self, action):
        motion = self.motions[action]
        current_position = self.maze.objects.agent.positions[0]
        new_position = [current_position[0] + motion[0], current_position[1] + motion[1]]
        valid = self._is_valid(new_position)
        if valid:
            self.maze.objects.agent.positions = [new_position]
        if self._is_goal(new_position):
            reward = +10
            done = True
        elif not valid:
            reward = -0.1
            done = False
        else:
            reward = -0.01
            done = False
        # d_s0 = manhattan_distance(current_position, self.maze.objects.goal.positions[0])
        # d_s1 = manhattan_distance(new_position, self.maze.objects.goal.positions[0])
        # shaping = GAMMA*(-d_s1) - (-d_s0)
        # shaping = shaping if self.shaping else 0
        # return self.maze.to_value(), reward + shaping, done, {}
        return self.maze.to_value(), reward, done, {}
        
    def reset(self):
        if self.randomize_start:
            self.maze.objects.agent.positions = [list(random.choice(self.maze.objects.free.positions))]
        else:
            self.maze.objects.agent.positions = [self.start_pos]
        if self.randomize_goal: 
            self.maze.objects.goal.positions = [list(random.choice(self.maze.objects.free.positions))]
        else:
            self.maze.objects.goal.positions = [self.goal_pos] 
        return self.maze.to_value()
    
    def _is_valid(self, position):
        nonnegative = position[0] >= 0 and position[1] >= 0
        within_edge = position[0] < self.maze.size[0] and position[1] < self.maze.size[1]
        passable = not self.maze.to_impassable()[position[0]][position[1]]
        return nonnegative and within_edge and passable
    
    def _is_goal(self, position):
        out = False
        for pos in self.maze.objects.goal.positions:
            if position[0] == pos[0] and position[1] == pos[1]:
                out = True
                break
        return out
    
    def get_image(self):
        return self.maze.to_rgb()











