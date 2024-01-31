<div style="text-align:center;">
  <img src="https://github.com/DanialSoleimany/TicTacToe_RL_Q-Learning/raw/main/tictactoe.png" alt="Tic Tac Toe">
</div>

# Reinforcement Learning for Tic-Tac-Toe using Q-Learning Algorithm

## Overview

This project implements a Tic-Tac-Toe game where AI players are trained to play against each other using reinforcement learning (Q-Learning Algorithm). The goal is to create AI players that can learn optimal strategies through self-play and compete against each other.

## Components of Project

### Human Player (human_player.py)
- The `HumanPlayer` class allows human interaction with the game.
- It prompts the user to input their desired position on the game board during gameplay.

### Judger (judger.py)
- The `Judger` class manages the game playing process and reward assignment between two players.
- It determines the winner of each game and assigns rewards to the players based on the outcome.

### AI Player (player.py)
- The `Player` class represents an AI player in the Tic-Tac-Toe game.
- It learns and improves its strategy through reinforcement learning techniques such as Q-learning.

### State (state.py)
- The `State` class represents the state of the Tic-Tac-Toe game board.
- It keeps track of the current game state and determines whether the game has ended.

### Training (training.py)
- The `train()` function in `main.py` trains AI players through self-play.
- It updates the players' strategies based on the outcomes of the games played.

## Usage

1. **Training AI Players**:
   - Run the `train()` function in `main.py` to train AI players through self-play.
   - During training, the players learn to improve their strategies by playing against each other.

2. **Competing AI Players**:
   - Use the `compete()` function in `main.py` to pit trained AI players against each other.
   - This allows you to evaluate the performance of the trained players without further learning.

3. **Playing Against AI**:
   - Use the `play()` function in `main.py` to play against the trained AI player.
   - You can interactively make moves against the AI and see the outcome of each game.
