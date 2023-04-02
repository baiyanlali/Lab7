# Lab7

This code represents a Python implementation of the Co-Evolutionary algorithm for playing the Iterated Prisoner's Dilemma game. The game is defined by four scores: R (reward for mutual cooperation), S (the score for the player who cooperates while the other defects), T (the score for the player who defects while the other cooperates), and P (punishment for mutual defection). The program consists of several functions that play the game and calculate the fitness of each strategy. It then uses a Co-Evolutionary algorithm to evolve two populations of players that compete against each other for better scores.

The Co-Evolutionary algorithm operates as follows: 
- It creates an initial population of random players for each population. 
- It plays the game for a fixed number of rounds, and then computes the average score of each player in each population. 
- It selects parents from each population based on their fitness score and produces offspring by taking the average of two selected parents. 
- It mutates each offspring with a fixed mutation rate. 
- It repeats this process for a given number of generations, keeping track of the average score for both player populations in each generation. 
- The algorithm outputs the final populations for both players.

The code also contains utility functions for encoding and decoding the strategies of the players and for creating the initial populations of players. It also provides a function for plotting the average score of each player population over the generations.

At the end of the code, the algorithm is run over the specified parameters for number of generations, population size, mutation rate, memory size, and number of rounds of the game. The final populations for both players are printed.

TODO: Please try to improve the convergence of the algorithm.
