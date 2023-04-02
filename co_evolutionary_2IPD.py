'''
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
'''

import numpy as np
import matplotlib.pyplot as plt


# Game settings
R = 3
S = 0
T = 5
P = 1

def play_2IPD(player1_move, player2_move):
    if player1_move and player2_move:
        return R, R
    elif not player1_move and player2_move:
        return S, T
    elif player1_move and not player2_move:
        return T, S
    else:
        return P, P

def encode_memory(memory):
    return sum(2**i * move for i, move in enumerate(memory))

def decode_memory(encoded_memory, memory_size):
    return [(encoded_memory >> i) & 1 for i in range(memory_size)]

def create_initial_population(pop_size, memory_size):
    return np.random.randint(0, 2, size=(pop_size, 2 ** memory_size))

def calculate_fitness(population1, population2, memory_size, num_rounds):
    fitness = np.zeros(len(population1))

    for i, player1_strategy in enumerate(population1):
        for j, player2_strategy in enumerate(population2):
            player1_memory = [0] * memory_size
            player2_memory = [0] * memory_size

            for round in range(num_rounds):
                player1_move = player1_strategy[encode_memory(player1_memory)]
                player2_move = player2_strategy[encode_memory(player2_memory)]

                player1_score, player2_score = play_2IPD(player1_move, player2_move)
                fitness[i] += player1_score

                player1_memory.pop(0)
                player1_memory.append(player2_move)

                player2_memory.pop(0)
                player2_memory.append(player1_move)

    return fitness

def mutation(parent, mutation_rate):
    return np.where(np.random.rand(*parent.shape) < mutation_rate, 1 - parent, parent)

def run_co_evolutionary_algorithm(num_generations, pop_size, mutation_rate, memory_size, num_rounds):
    player1_population = create_initial_population(pop_size, memory_size)
    player2_population = create_initial_population(pop_size, memory_size)

    player1_scores = []
    player2_scores = []

    for generation in range(num_generations):
        player1_fitness = calculate_fitness(player1_population, player2_population, memory_size, num_rounds)
        player2_fitness = calculate_fitness(player2_population, player1_population, memory_size, num_rounds)

        player1_scores.append(np.mean(player1_fitness))
        player2_scores.append(np.mean(player2_fitness))

        # Selection and crossover
        parent_indices = np.random.choice(len(player1_population), size=(len(player1_population), 2), p=player1_fitness / player1_fitness.sum())
        player1_population = np.array([mutation((player1_population[p1] + player1_population[p2]) // 2, mutation_rate) for p1, p2 in parent_indices])

        parent_indices = np.random.choice(len(player2_population), size=(len(player2_population), 2), p=player2_fitness / player2_fitness.sum())
        player2_population = np.array([mutation((player2_population[p1] + player2_population[p2]) // 2, mutation_rate) for p1, p2 in parent_indices])

    plt.plot(player1_scores, label="Player 1")
    plt.plot(player2_scores, label="Player 2")
    plt.xlabel("Generation")
    plt.ylabel("Average Score")
    plt.legend()
    plt.show()

    return player1_population, player2_population

if __name__ == "__main__":
    # Parameters
    num_generations = 100
    pop_size = 50
    mutation_rate = 0.1
    memory_size = 3
    num_rounds = 50

    # Run co-evolutionary algorithm
    print("Running co-evolutionary algorithm...")
    player1_population, player2_population = run_co_evolutionary_algorithm(num_generations, pop_size, mutation_rate, memory_size, num_rounds)

    # Print final populations
    print("Player 1 final population:")
    print(player1_population)

    print("Player 2 final population:")
    print(player2_population)

