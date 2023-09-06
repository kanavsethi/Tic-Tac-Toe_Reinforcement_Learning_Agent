# Tic-Tac-Toe_Reinforcement_Learning_Agent

## Tic-Tac-Toe Playing Bot Trained using Reinforcement Learning

Welcome to the Tic-Tac-Toe Playing Bot trained using Reinforcement Learning! This project implements a game of Numerical Tic-Tac-Toe. Instead of the traditional X and O, the numbers 1 to 9 are used. In the 3x3 grid, numbers 1 to 9 are filled, with one number in each cell. The first player plays with the odd numbers, the second player plays with the even numbers, i.e. player 1 can enter only an odd number in the cell while player 2 can enter an even number in one of the remaining cells. Each number can be used exactly once in the entire grid. The player who puts down 15 points in a line - (column, row or a diagonal) wins the game.

During Training:
We have two players: a Reinforcement Learning (RL) agent as Player 1 and the environment as Player 2, each with their own set of Odd and Even numbers respectively.

Post Deployment:
We have two players: a Reinforcement Learning (RL) agent as Player 1 and User as Player 2, each with their own set of Odd and Even numbers respectively.


## Game Rules

In this version of Tic-Tac-Toe, the game is played on a 3x3 grid using numbers from 1 to 9. These numbers can only be used once throughout the game. Here are the key rules:

1. **Grid**: The game is played on a 3x3 grid consisting of 9 cells.

2. **Players**: There are two players - the RL agent and the environment/user. The RL agent uses odd numbers {1, 3, 5, 7, 9}, while the environment/user uses even numbers {2, 4, 6, 8}.

3. **Turns**: The player with odd numbers always goes first. Each player takes turns to place one unused number on an empty spot on the grid.

4. **Objective**: The objective is to make 15 points in a row, column, or diagonal. Players can use their own numbers or the opponent's numbers in the grid to achieve this goal.

5. **Game Termination**: The game terminates when one of the players makes 15 points.

## Reward Structure

The RL agent receives rewards based on the following structure:

- **+10**: If the agent wins by making 15 points first.
- **-10**: If the environment wins by making 15 points first.
- **0**: If the game ends in a draw, meaning neither player is able to make 15, and the board is completely filled.
- **-1**: For each move the agent takes during the game.

## Note

One important aspect to note is that the current implementation of the agent only learns to play with odd values. If you wish to implement an agent that can play with even values as well, you can modify the implementation by switching around some values. 
Keep in mind that training an agent to handle both odd and even values will take twice as long but is certainly possible.

Feel free to explore, modify, and experiment with this Tic-Tac-Toe Playing Bot trained using Reinforcement Learning. Have fun playing the game and experimenting with different reward structures and hyperparamter values! If you have any questions or feedback, please don't hesitate to reach out.

Happy gaming!
