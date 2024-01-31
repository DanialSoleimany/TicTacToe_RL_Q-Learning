from player import Player
from judger import Judger

"""Module for training AI players."""
def train(epochs=20000):
    """Train two AI players to play Tic-Tac-Toe against each other."""
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
