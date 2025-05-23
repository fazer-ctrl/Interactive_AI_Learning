"""
Connect Four Game
Based on the AIMA-Python implementation (https://github.com/aimacode/aima-python)
Extended and modified by Dakota Ling, 2024
with assistance from Claude AI (Anthropic, PBC)
"""

import time
import random
from games4e import ConnectFour, alpha_beta_cutoff_search, monte_carlo_tree_search

TIME_LIMIT = 15  # seconds
MAX_TURNS = 100  # Maximum number of turns per game

def time_limited_alpha_beta_search(game, state):
    print("Alpha-Beta thinking...")
    def cutoff_test(state, depth):
        return depth > 1000 or time.time() > end_time

    end_time = time.time() + TIME_LIMIT
    move = alpha_beta_cutoff_search(state, game, d=1000, cutoff_test=cutoff_test, eval_fn=lambda s: game.utility(s, game.to_move(game.initial)))
    print(f"Alpha-Beta chose move: {move}")
    return move

def time_limited_monte_carlo_search(game, state):
    print("Monte Carlo thinking...")
    end_time = time.time() + TIME_LIMIT
    best_move = None
    while time.time() < end_time:
        move = monte_carlo_tree_search(state, game)
        if move is not None:
            best_move = move
    if best_move is None:
        best_move = random.choice(game.actions(state))
    print(f"Monte Carlo chose move: {best_move}")
    return best_move

def play_game(game, player1, player2):
    state = game.initial
    turn_count = 0
    while turn_count < MAX_TURNS:
        for player in (player1, player2):
            print(f"Turn {turn_count + 1}")
            game.display(state)
            move = player(game, state)
            if move is None or move not in game.actions(state):
                print(f"Invalid move: {move}")
                return 0  # Draw if invalid move
            state = game.result(state, move)
            if game.terminal_test(state):
                game.display(state)
                return game.utility(state, game.to_move(game.initial))
            turn_count += 1
    print("Game exceeded maximum turns")
    return 0  # Draw if game goes on too long

def compare_agents(num_games=30):
    game = ConnectFour()
    results = []

    for i in range(num_games):
        print(f"\nPlaying game {i+1}/{num_games}")
        if i % 2 == 0:
            result = play_game(game, time_limited_alpha_beta_search, time_limited_monte_carlo_search)
            results.append(result)
        else:
            result = play_game(game, time_limited_monte_carlo_search, time_limited_alpha_beta_search)
            results.append(-result)  # Negate the result when Monte Carlo plays first
        print(f"Game {i+1} result: {result}")

    alpha_beta_wins = sum(1 for r in results if r > 0)
    monte_carlo_wins = sum(1 for r in results if r < 0)
    draws = sum(1 for r in results if r == 0)

    print(f"\nFinal Results:")
    print(f"Alpha-Beta wins: {alpha_beta_wins}")
    print(f"Monte Carlo wins: {monte_carlo_wins}")
    print(f"Draws: {draws}")

if __name__ == "__main__":
    compare_agents()