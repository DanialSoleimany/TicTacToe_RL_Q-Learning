#######################################################################
# Copyright (C)                                                       #
# 2016 Shangtong Zhang(zhangshangtong.cpp@gmail.com)                  #
# 2016 Jan Hakenberg(jan.hakenberg@gmail.com)                         #
# 2016 Tian Jun(tianjun.cpp@gmail.com)                                #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

from state import BOARD_ROWS, BOARD_COLS, getAllStates
from player import Player
from human_player import HumanPlayer
from judger import Judger

"""Train, compete, and play Tic-Tac-Toe using reinforcement learning."""

def train(epochs=10000):
    """Train two AI players through self-play.

    This function trains two AI players by making them play against each other
    through self-play. During each epoch, the players learn to improve their
    strategies by updating their estimations based on the outcomes of the games.

    Args:
        epochs (int): Number of training epochs (default is 10,000).
    """
    player1 = Player()
    player2 = Player()
    judger = Judger(player1, player2)
    player1Win = 0.0
    player2Win = 0.0
    for i in range(0, epochs):
        print("Epoch", i)
        winner = judger.play()
        if winner == 1:
            player1Win += 1
        if winner == -1:
            player2Win += 1
        judger.reset()
    print(player1Win / epochs)
    print(player2Win / epochs)
    player1.savePolicy()
    player2.savePolicy()

def compete(turns=10):
    """Compete two trained AI players against each other.

    This function pits two trained AI players against each other to evaluate
    their performance. Both players use their learned strategies to compete
    without further learning. The function prints out the win rates of each
    player after the competition.

    Args:
        turns (int): Number of competition turns (default is 10).
    """
    player1 = Player(exploreRate=0)
    player2 = Player(exploreRate=0)
    judger = Judger(player1, player2, False)
    player1.loadPolicy()
    player2.loadPolicy()
    player1Win = 0.0
    player2Win = 0.0

    for i in range(0, turns):
        print("Epoch", i)
        winner = judger.play()
        if winner == 1:
            player1Win += 1
        if winner == -1:
            player2Win += 1
        judger.reset()

    print(player1Win / turns)
    print(player2Win / turns)

def play():
    """Play against the trained AI player.

    This function allows a human player to play against the trained AI player.
    It loads the trained policy of the AI player and enables the human player
    to make moves interactively. After each game, it prints out the result
    (win, lose, or tie) for the human player.
    """
    while True:
        player1 = Player(exploreRate=0)
        player2 = HumanPlayer()
        judger = Judger(player1, player2, False)
        player1.loadPolicy()
        winner = judger.play(True)

        if winner == player2.symbol:
            print("Win!")
        elif winner == player1.symbol:
            print("Lose!")
        else:
            print("Tie!")

if __name__ == "__main__":
    train()
    compete()
    play()
