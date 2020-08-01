# `mazelab`: A customizable framework to create maze and gridworld environments.

This is a fork of [zuoxingdong/mazelab](https://github.com/zuoxingdong/mazelab), and defines several maze gym environments with visual inputs:
1. `EmptyMaze-10x10-FixedGoal-v0`
2. `EmptyMaze-10x10-FixedGoal-NonTerminating-v0`
3. `EmptyMaze-10x10-RandomGoal-v0`
4. `Maze-10x10-FixedGoal-v0`
5. `Maze-10x10-FixedGoal-NonTerminating-v0`
6. `Maze-10x10-RandomGoal-v0`
7. `Maze-15x15-FixedGoal-v0`
8. `Maze-15x15-FixedGoal-NonTerminating-v0`
9. `Maze-15x15-RandomGoal-v0`
10. `Maze-25x25-FixedGoal-v0`
11. `Maze-25x25-RandomGoal-v0`
12. `RandomMaze-7x7-FixedGoal-v0`
13. `RandomMaze-7x7-FixedGoal-NonTerminating-v0`
14. `RandomMaze-7x7-RandomGoal-v0`
15. `RandomMaze-8x8-FixedGoal-v0`
16. `RandomMaze-8x8-FixedGoal-NonTerminating-v0`
17. `RandomMaze-8x8-RandomGoal-v0`

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


