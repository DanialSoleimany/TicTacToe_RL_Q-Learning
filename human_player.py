from state import BOARD_COLS, State

"""Class representing a human player in the Tic-Tac-Toe game."""
class HumanPlayer:
    def __init__(self, stepSize=0.1, exploreRate=0.1):
        """Initialize the HumanPlayer object.

        Args:
            stepSize (float, optional): Step size to update estimations (default is 0.1).
            exploreRate (float, optional): Possibility to explore (default is 0.1).
        """
        self.symbol = None
        self.currentState = None

    def reset(self):
        """Reset the player's internal state."""
        pass

    def setSymbol(self, symbol):
        """Set the symbol (X or O) for the player.

        Args:
            symbol (int): The symbol assigned to the player (1 for X, -1 for O).
        """
        self.symbol = symbol

    def feedState(self, state):
        """Receive the current state of the game.

        Args:
            state (State): The current state of the game board.
        """
        self.currentState = state

    def feedReward(self, reward):
        """Receive the reward after a game ends.

        Args:
            reward (float): The reward received after the game ends.
        """
        pass

    def takeAction(self):
        """Take action based on user input.

        This method prompts the user to input their desired position on the game board
        and converts it into a valid move (row, column, symbol) for the game.

        Returns:
            tuple: A tuple containing the row index, column index, and the player's symbol.
        """
        data = int(input("Input your position:"))
        data -= 1
        i = data // BOARD_COLS
        j = data % BOARD_COLS

        if self.currentState.data[i, j] != 0:
            return self.takeAction()
        
        return (i, j, self.symbol)
