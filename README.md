# `mazelab`: A customizable framework to create maze and gridworld environments.

This is a fork of [zuoxingdong/mazelab](https://github.com/zuoxingdong/mazelab), and defines several maze gym environments with greyscale image observation spaces.

**Mazes with no walls**
* `EmptyMaze-10x10-FixedGoal-v3`
* `EmptyMaze-10x10-CoinFlipGoal-v3`
* `EmptyMaze-10x10-TwoGoals-v3`
* `EmptyMaze-10x10-RandomGoal-v3`

as well as NonTerminating variants like:
* `EmptyMaze-10x10-FixedGoal-NonTerminating-v3`
* `...`

**Mazes with fixed walls**
* 10x10
    * `Maze-10x10-FixedGoal-v3`
    * `Maze-10x10-CoinFlipGoal-v3`
    * `Maze-10x10-TwoGoals-v3`
    * `Maze-10x10-RandomGoal-v3`

* 15x15
    * `Maze-15x15-FixedGoal-v3`
    * `Maze-15x15-CoinFlipGoal-v3`
    * `Maze-15x15-TwoGoals-v3`
    * `Maze-15x15-RandomGoal-v3`

* 25x25
    * `Maze-25x25-FixedGoal-v3`
    * `Maze-25x25-CoinFlipGoal-v3`
    * `Maze-25x25-TwoGoals-v3`
    * `Maze-25x25-RandomGoal-v3`

as well as NonTerminating variants of each
* `...`

**Mazes with walls which change on reset**
* 7x7
    * `RandomMaze-7x7-FixedGoal-v3`
    * `RandomMaze-7x7-CoinFlipGoal-v3`
    * `RandomMaze-7x7-RandomGoal-v3`

* 8x8
    * `RandomMaze-8x8-FixedGoal-v3`
    * `RandomMaze-8x8-CoinFlipGoal-v3`
    * `RandomMaze-8x8-RandomGoal-v3`

as well as NonTerminating variants of each
* `...`

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
env = gym.make('Maze-10x10-FixedGoal-v3')
```


