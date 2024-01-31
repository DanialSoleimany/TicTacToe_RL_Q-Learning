from state import State, getAllStates

"""Class to manage game playing and reward assignment between two players."""
class Judger:
    def __init__(self, player1, player2, feedback=True):
        """Initialize the Judger object.

        Args:
            player1 (Player): The first player.
            player2 (Player): The second player.
            feedback (bool, optional): Whether to provide feedback to the players after each game. 
                Defaults to True.
        """
        self.p1 = player1
        self.p2 = player2
        self.feedback = feedback
        self.currentPlayer = None
        self.p1Symbol = 1
        self.p2Symbol = -1
        self.p1.setSymbol(self.p1Symbol)
        self.p2.setSymbol(self.p2Symbol)
        self.currentState = State()
        self.allStates = getAllStates()

    def giveReward(self):
        """Assign rewards to players based on the outcome of the game."""
        if self.currentState.winner == self.p1Symbol:
            self.p1.feedReward(1)
            self.p2.feedReward(0)
        elif self.currentState.winner == self.p2Symbol:
            self.p1.feedReward(0)
            self.p2.feedReward(1)
        else:
            self.p1.feedReward(0.1)
            self.p2.feedReward(0.5)

    def feedCurrentState(self):
        """Feed the current state to both players."""
        self.p1.feedState(self.currentState)
        self.p2.feedState(self.currentState)

    def reset(self):
        """Reset the game state and player states."""
        self.p1.reset()
        self.p2.reset()
        self.currentState = State()
        self.currentPlayer = None

    def play(self, show=False):
        """Play a game between the two players.

        Args:
            show (bool, optional): Whether to print the game board during the game. 
                Defaults to False.

        Returns:
            int: The winner of the game (1 for player 1, -1 for player 2, 0 for tie).
        """
        self.reset()
        self.feedCurrentState()
        while True:
            if self.currentPlayer == self.p1:
                self.currentPlayer = self.p2
            else:
                self.currentPlayer = self.p1
            if show:
                self.currentState.show()
            [i, j, symbol] = self.currentPlayer.takeAction()
            self.currentState = self.currentState.nextState(i, j, symbol)
            hashValue = self.currentState.getHash()
            self.currentState, isEnd = self.allStates[hashValue]
            self.feedCurrentState()
            if isEnd:
                if self.feedback:
                    self.giveReward()
                return self.currentState.winner
