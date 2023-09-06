import numpy as np
import random
from itertools import groupby
from itertools import product


"""
Rules
----------

1. The game will be played on a 3x3 grid (9 cells) using numbers from 1 to 9. Each number can be used exactly once in the entire grid.

2. There are two players: one is the Reinforcement Learning (RL) agent and other is the environment.

3. The RL agent is given odd numbers {1, 3, 5, 7, 9} and the environment is given the even numbers {2, 4, 6, 8}

4. Each of them takes a turn. The player with odd numbers always goes first.

5. At each round, a player puts one unused number on a blank spot.

6. The objective is to make 15 points in a row, column or a diagonal. The player can use the opponent's numbers in the grid to make 15.

7. The game terminates when any one of the players makes 15.


Reward Structure:

+10 if the agent wins (makes 15 points first)

-10 if the environment wins

0 if the game ends in a draw (no one is able to make 15 and the board is filled up)

-1 for each move agent takes

"""







class TicTacToe():

    def __init__(self):
        """initialise the board"""
        
        # initialise state as an array
        self.state = [np.nan for _ in range(9)]  # initialises the board position, can initialise to an array or matrix
        # all possible numbers
        self.all_possible_numbers = [i for i in range(1, len(self.state) + 1)] # , can initialise to an array or matrix

        self.reset()


    def is_winning(self, curr_state):
        """Takes state as an input and returns whether any row, column or diagonal has winning sum
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan]
        Output = False"""
        win=False
        #Check Rows and columns
        for i in range(0,3):
            if not np.isnan(curr_state[i*3]) and not np.isnan(curr_state[(i*3)+1]) and not np.isnan(curr_state[(i*3)+2]) and  np.sum([curr_state[i*3],curr_state[(i*3)+1],curr_state[(i*3)+2]]) == 15: # Check Rows
                print("Win")
                win=True                                                    
                break
            elif not np.isnan(curr_state[i]) and not np.isnan(curr_state[i+3]) and not np.isnan(curr_state[i+6]) and np.sum([curr_state[i],curr_state[i+3],curr_state[i+6]]) == 15: # Check Columns
                print("Win")
                win=True                                                    
                break
        if not win:
            if not np.isnan(curr_state[0]) and not np.isnan(curr_state[4]) and not np.isnan(curr_state[8]) and np.sum([curr_state[0],curr_state[4],curr_state[8]]) == 15: # Check Diagonal 1
                print("Win")
                win=True
            elif not np.isnan(curr_state[2]) and not np.isnan(curr_state[4]) and not np.isnan(curr_state[6]) and np.sum([curr_state[2],curr_state[4],curr_state[6]]) == 15: # Check Diagonal 2
                print("Win")
                win=True
        return win
 

    def is_terminal(self, curr_state):
        
        # Terminal state could be winning state or when the board is filled up

        if self.is_winning(curr_state) == True:
            return True, 'Win'

        elif len(self.allowed_positions(curr_state)) ==0:
            return True, 'Tie'

        else:
            return False, 'Resume'


    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        return [i for i, val in enumerate(curr_state) if np.isnan(val)]


    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""

        used_values = [val for val in curr_state if not np.isnan(val)]
        agent_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 !=0] # Only Odd Numbers
        env_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 ==0] # Only Even Numbers

        return (agent_values, env_values)


    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions, i.e, all combinations of allowed positions and allowed values"""

        agent_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[0])
        env_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[1])
        return (agent_actions, env_actions)



    def state_transition(self, curr_state, curr_action):
        """Takes current state and action and returns the board position just after agent's move.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = [1, 2, 3, 4, nan, nan, nan, 9, nan]
        """
        curr_state[curr_action[0]]=curr_action[1]
        return curr_state


    def step(self, curr_state, curr_action):
        """Takes current state and action and returns the next state, reward and whether the state is terminal. Hint: First, check the board position after
        agent's move, whether the game is won/loss/tied. Then incorporate environment's move and again check the board status.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = ([1, 2, 3, 4, nan, nan, nan, 9, nan], -1, False)"""
        
        # Add initial_step function for Even Agent
        # Update order of below functions
        
        
        new_state = self.state_transition(curr_state, curr_action)
        print(f"New State : {new_state}") # Post Agents Action
        endGame,reason = self.is_terminal(new_state)
        
        if not endGame: # Not Agent Win or Tie
            
            # Choose Random Position and Random Action (Even Number)
            
            position = random.choice(self.allowed_positions(new_state)) 
            action = random.choice(self.allowed_values(new_state)[1]) # Switch 1 for 0 for Even Agent

            env_state = self.state_transition(new_state, [position,action]) # Take Action, State post Env Action
            
            envendGame,reason = self.is_terminal(env_state) 
            
            if not endGame:
                return env_state, -1 , endGame # No Win, single Step Taken
            else:
                if reason=='Tie':
                    return curr_state, 0, endGame
                else:
                    return curr_state, -10, endGame # Env Win
            
        else: # Agent Win or Tie
            if reason=='Tie':
                return curr_state, 0, endGame
            else:
                return curr_state, 10, endGame # Agent Win

    #Uncomment Below for Even Agent
    """This functions will be used only if environment is playing with the odd numbers, i.e., the environment has to make first move"""
    # def initial_step(self, curr_state):

    #     value = random.choice(self.allowed_values(curr_state)[0])
    #     position = random.choice([i for i in self.allowed_positions(curr_state)])

    #     curr_state[position] = value
    #     return curr_state

    def reset(self):
        return self.state
