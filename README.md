# 2048-Game AI

## Introduction

2048 is a single-player sliding block puzzle game. The game's objective is to slide numbered tiles on a grid to combine them to create a tile with the number 2048. The numbers are in powers of 2; the game ends when there are no other moves left to combine the tiles. The project satisfies two requirements: Searching and First order logic. There are two agents here, namely Player and Computer.

## Design

The design used to implement the game draws contrast between two different search algorithms and between two agents with certain heuristics. These are considered by understanding the game, where the player should try to get a high score by combining tiles of similar numbers. Understanding its functionality and its search tree, I had decided to make the comparison between the two different search algorithms, Minimax and Minimax with alpha-beta pruning. 

Minimax Algorithm: It assumes that the computer opponent is perfect in minimizing player's outcome. This is done irrespective of whether the opponent is perfect in doing so. 

This algorithm assumes that there are two players. One is named the Min and the other one is the Max. Both the players alternate in turms. The Max moves first. The aim of max is to maximize a heuristic score and that of min is to minimize the same. For every player, a minimax value is computed. This value is the best achievable payoff against his play. The move with the optimum minimax value is chosen by the player.

Usually, the number of nodes to be explored by this algorithm is huge. In order to optimize it, pruning is used.

Minimax with alpha-beta pruning: This needs to be implemented to speed up the search process by eliminating irrelevant branches. Since the search space is huge (the Player AI agent can take any of the 4 actions LEFT, RIGHT, TOP, DOWN and the Computer Player can choose any free tile randomly and fill it with either 2 or 4), it will be very expensive to search all the branches.

The First Order Logic was implemented with a prolog. It helps us understand how actions and results connect. For example, in the code based on the number the action occurs. That is, it could move up, down, left and right.

### Heuristics Considered:

1.Check for empty tiles,this should be done because the agent can have an idea what move to choose so that he can maintain more empty spaces.
2.Property of monotonicity - this is evaluated so that there is no high value that is present in between two small values making it harder to combine the tiles. 
3.Making sure that the maximum tile is in the corner of the grid, it helps to get a maximum score.


## Environment:

Python3

## How to Execute:

Can run the game using 2048.py and 2048withoutpruning.py. 

Execute the python code 2048withoutpruning.py and 2048.py in python to compare how the game works with two different search algorithms.

The 2048samleprolog.pl is a sample part of the prolog code.
