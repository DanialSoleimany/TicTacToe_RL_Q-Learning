import numpy as np
import pickle
from state import State, BOARD_ROWS, BOARD_COLS, getAllStates

"""Class representing an AI player in the Tic-Tac-Toe game."""
class Player:
    def __init__(self, stepSize=0.1, exploreRate=0.1):
        """Initialize the Player object.

        Args:
            stepSize (float, optional): Step size to update estimations (default is 0.1).
            exploreRate (float, optional): Possibility to explore (default is 0.1).
        """
        self.allStates = getAllStates()
        self.estimations = dict()
        self.stepSize = stepSize
        self.exploreRate = exploreRate
        self.states = []

    def reset(self):
        """Reset the player's internal state."""
        self.states = []

    def setSymbol(self, symbol):
        """Set the symbol (X or O) for the player.

        Args:
            symbol (int): The symbol assigned to the player (1 for X, -1 for O).
        """
        self.symbol = symbol
        for hash in self.allStates.keys():
            (state, isEnd) = self.allStates[hash]
            if isEnd:
                if state.winner == self.symbol:
                    self.estimations[hash] = 1.0
                else:
                    self.estimations[hash] = 0
            else:
                self.estimations[hash] = 0.5

    def feedState(self, state):
        """Receive the current state of the game.

        Args:
            state (State): The current state of the game board.
        """
        self.states.append(state)

    def feedReward(self, reward):
        """Receive the reward after a game ends.

        Args:
            reward (float): The reward received after the game ends.
        """
        if len(self.states) == 0:
            return
        self.states = [state.getHash() for state in self.states]
        target = reward
        for latestState in reversed(self.states):
            value = self.estimations[latestState] + self.stepSize * (target - self.estimations[latestState])
            self.estimations[latestState] = value
            target = value
        self.states = []

    def takeAction(self):
        """Determine the next action to take based on the current state.

        Returns:
            tuple: A tuple containing the row index, column index, and the player's symbol for the next action.
        """
        state = self.states[-1]
        nextStates = []
        nextPositions = []
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if state.data[i, j] == 0:
                    nextPositions.append([i, j])
                    nextStates.append(state.nextState(i, j, self.symbol).getHash())
        if np.random.binomial(1, self.exploreRate):
            np.random.shuffle(nextPositions)
            self.states = []
            action = nextPositions[0]
            action.append(self.symbol)
            return action

        values = []
        for hash, pos in zip(nextStates, nextPositions):
            values.append((self.estimations[hash], pos))
        np.random.shuffle(values)
        values.sort(key=lambda x: x[0], reverse=True)
        action = values[0][1]
        action.append(self.symbol)
        return action

    def savePolicy(self):
        """Save the learned policy of the player to a file."""
        fw = open('optimal_policy_' + str(self.symbol), 'wb')
        pickle.dump(self.estimations, fw)
        fw.close()

    def loadPolicy(self):
        """Load the learned policy of the player from a file."""
        fr = open('optimal_policy_' + str(self.symbol), 'rb')
        self.estimations = pickle.load(fr)
        fr.close()
