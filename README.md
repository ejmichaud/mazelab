# `mazelab`: A customizable framework to create maze and gridworld environments.

This is a fork of [zuoxingdong/mazelab](https://github.com/zuoxingdong/mazelab), and defines several maze gym environments with greyscale image observation spaces.

**Mazes with no walls**
* `EmptyMaze-10x10-FixedGoal-v0`
* `EmptyMaze-10x10-FixedGoal-NonTerminating-v0`
* `EmptyMaze-10x10-RandomGoal-v0`
* `EmptyMaze-10x10-CoinFlipGoal-NonTerminating-v0`

**Mazes with fixed walls**
* `Maze-10x10-FixedGoal-v0`
* `Maze-10x10-FixedGoal-NonTerminating-v0`
* `Maze-10x10-RandomGoal-v0`
* `Maze-10x10-CoinFlipGoal-NonTerminating-v0`
* `Maze-15x15-FixedGoal-v0`
* `Maze-15x15-FixedGoal-NonTerminating-v0`
* `Maze-15x15-RandomGoal-v0`
* `Maze-15x15-CoinFlipGoal-NonTerminating-v0`
* `Maze-25x25-FixedGoal-v0`
* `Maze-25x25-RandomGoal-v0`

**Mazes with walls which change on reset**
* `RandomMaze-7x7-FixedGoal-v0`
* `RandomMaze-7x7-FixedGoal-NonTerminating-v0`
* `RandomMaze-7x7-RandomGoal-v0`
* `RandomMaze-7x7-CoinFlipGoal-NonTerminating-v0`
* `RandomMaze-8x8-FixedGoal-v0`
* `RandomMaze-8x8-FixedGoal-NonTerminating-v0`
* `RandomMaze-8x8-RandomGoal-v0`
* `RandomMaze-8x8-CoinFlipGoal-NonTerminating-v0`

# Installation

First clone the repo:
```
git clone https://github.com/ejmichaud/mazelab
```
Then from the repo root directory:
```
pip install -e .
```

# Usage

Once installed, simply import:
```python
import gym
import mazelab
```
This will create and register the maze environments `1-6` listed above. To create an environment, you can then simply execute:
```python
env = gym.make('Maze-10x10-FixedGoal-v0')
```


