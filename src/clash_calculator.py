import math

from typing import Tuple

SANITY_AFFECT = 0.45

# pydantic model later? we can create a DB of skills
class Skill:
    num_of_coins: int
    base_strength: int
    coin_strength: int

    def __init__(self, num_of_coins: int, base_strength: int, coin_strength: int):
        self.num_of_coins = num_of_coins
        self.base_strength = base_strength
        self.coin_strength = coin_strength

test_skill_1 = Skill(3, 4, 2)
test_skill_2 = Skill(2, 4, 3)

# Calculates coin flip possibilites using (n choose k)(p)^s(1 - p)^f
# TODO: Take into consideration the possibility that sanity affects first coin flip only (???? why pm WHY)
def outcome_probability(total_coins: int, heads: int, probability_of_heads: float):
    combinations = math.comb(total_coins, heads)
    success = probability_of_heads ** heads
    failure = (1 - probability_of_heads) ** (total_coins - heads)
    return combinations * success * failure


# basic algo
# we have player coins, we should determine chance of getting X result
# then take opponent coins, determine result of getting Y result
# win is obviously player strength > opponent strength

# TODO: On clash win, we repeat the clash but with a coin removed, similar on a clash lose

def clash_outcome(
    player_skill: Skill,
    opponent_skill: Skill,
    player_sanity: int,
    player_coin_wins: int,
    opponent_sanity: int = 0,
):
    if player_coin_wins > player_skill.num_of_coins:
        print("oi u cheater")
        return
    # Sanity modifiers???
    player_success = 0.5 + ((SANITY_AFFECT * player_sanity) / 100)
    prob_player_coin = outcome_probability(player_skill.num_of_coins, player_coin_wins, player_success)
    total_player_strength = player_skill.base_strength + (player_coin_wins * player_skill.coin_strength)

    opponent_success = 0.5 + ((SANITY_AFFECT * opponent_sanity) / 100)
    possible_opponent_outcomes = {}
    for coins in range(0, opponent_skill.num_of_coins + 1):
        opponent_strength = opponent_skill.base_strength + (coins * opponent_skill.coin_strength)
        win = total_player_strength > opponent_strength
        status = ""
        if total_player_strength > opponent_strength:
            status = "Win"
        elif total_player_strength == opponent_strength:
            status = "Tie"
        else:
            status = "Lose"
        print(total_player_strength, opponent_strength)
        probability = outcome_probability(opponent_skill.num_of_coins, coins, opponent_success)
        possible_opponent_outcomes[coins] = (coins, status, probability)
    return(prob_player_coin, possible_opponent_outcomes)


print(clash_outcome(test_skill_1, test_skill_2, 45, 3))



def clash_calculator(
    num_of_player_coins: int,
    num_of_opponent_coins: int,
    player_coin_strength: int,
    opponent_coin_strength: int,
    player_modifier: int,
    opponent_modifier: int,
):
    pass