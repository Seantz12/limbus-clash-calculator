import math

from typing import Tuple


# basic algo
# we have player coins, we should determine chance of getting X result
# then take opponent coins, determine result of getting Y result
# win is obviously player strength > opponent strength



def clash_outcome(
    num_of_player_coins: int,
    num_of_opponent_coins: int,
    player_coin_strength: int,
    opponent_coin_strength: int,
    player_modifier: int,
    opponent_modifier: int,
    player_base_strength: int,
    opponent_base_strength: int,
    player_coin_wins: int,
):
    # Sanity modifiers???
    success = 0.5
    prob_player_coin = math.comb(num_of_player_coins, player_coin_wins) * (0.5 ** player_coin_wins) * (0.5 ** (num_of_player_coins - player_coin_wins))
    total_player_strength = player_base_strength + (player_coin_wins * player_coin_strength)
    possible_opponent_outcomes = {}
    for coins in range(0, num_of_opponent_coins + 1):
        opponent_strength = opponent_base_strength + (coins * opponent_coin_strength)
        win = total_player_strength > opponent_strength
        probability = math.comb(num_of_opponent_coins, coins) * (0.5 ** coins) * (0.5 ** (num_of_opponent_coins - coins))
        possible_opponent_outcomes[coins] = (coins, "Win" if win else "Lose", probability)
    return(prob_player_coin, possible_opponent_outcomes)

print(clash_outcome(3, 1, 2, 8, 0, 0, 3, 4, 3))

def clash_calculator(
    num_of_player_coins: int,
    num_of_opponent_coins: int,
    player_coin_strength: int,
    opponent_coin_strength: int,
    player_modifier: int,
    opponent_modifier: int,
):
    pass