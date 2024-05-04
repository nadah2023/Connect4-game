# Connect4-game
## Problem Summary:

A Connect 4 game with three difficulty levels: easy, medium, and hard. At the easy level, the game uses a random algorithm to make moves. The computer player selects a random column to drop its token into, without considering any strategic decision-making. At the medium level, the game uses the alpha-beta pruning algorithm. This algorithm enhances the search process by evaluating the best possible moves based on a scoring system. It explores the game tree, considering both maximizing and minimizing moves, and discards branches that are guaranteed to be worse than previously explored branches. On the hard level, the game uses the Minimax algorithm. This algorithm exhaustively evaluates all possible moves and their outcomes by simulating the game until its conclusion. It considers all possible moves and their consequences in choosing the best move for the computer player, assuming optimal play from both players. These difficulty levels provide varying levels of challenge for players, with the hard level employing a more sophisticated strategy to maximize the computer player's chances of winning.

## Methodology:

A Connect Four game with a graphical user interface (GUI) implemented using the Tkinter library. The game has three levels (easy, medium, hard), and there is also an option to play a typical game against an AI opponent or with another player or play Ai against Ai.

### The random algorithm at an easy level: 
A random algorithm is a simple approach to playing Connect 4, requiring minimal strategy and experimentation. It's suitable for beginners and It's important to note that a random algorithm is not likely to be very effective against more skilled players or more advanced algorithms that use strategic decision-making.  Here is how it works: 
The computer player selects a random column to drop its token into, without considering any strategic decision-making. chances of winning.

### alpha-beta pruning algorithm at the medium level: 
The alpha-beta pruning algorithm is a powerful technique for searching game trees and finding optimal moves in games with multiple alternative moves. It reduces the search tree size and eliminates the need to analyze all potential game pathways. 
Here is how it works:
 The algorithm starts by exploring the game tree, evaluating each node using a heuristic function. It tracks alpha and beta values, which represent the best maximum and minimum values. If a node has a score below beta, it prunes that branch, and if it finds a higher alpha value, it prunes that branch. The algorithm updates alpha and beta values until it reaches the maximum depth or prunes unlikely branches. It then chooses the move with the highest score based on the evaluation function and returns it as the best move for the current player.

### Minimax algorithm on the hard level: 
The minimax algorithm is used in game theory and decision-making to determine the best course of action provided that the adversary plays effectively as well.
 Here is how it works:
The algorithm constructs a game tree representing possible moves and outcomes from the current board state. It evaluates each node using a heuristic function, assigning a score based on the current position of pieces. The algorithm alternates between maximizing and minimizing the score at each level, choosing the move with the highest score for the maximizing player and the lowest score for the minimizing player. The algorithm explores the tree recursively until it reaches a terminal state, where it assigns a score based on the heuristic function. The algorithm propagates the scores back up the tree, choosing the move with the highest score for the maximizing player and the lowest score for the minimizing player.

## GUI:



![image](https://github.com/nadah2023/Connect4-game/assets/122016066/972b9f2f-8412-40b7-9e28-66ab5491d819)
![image](https://github.com/nadah2023/Connect4-game/assets/122016066/9f8d1762-6003-45fa-a957-9d7d6b5927a9)
![image](https://github.com/nadah2023/Connect4-game/assets/122016066/c9da3ba8-e152-495f-8e90-a03c3670a132)

