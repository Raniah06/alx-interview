#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given total
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins to make up a given total.

    Args:
        coins (list): The coin denominations.
        total (int): The target amount.

    Returns:
        int: The minimum number of coins needed to meet the total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    num_coins = 0

    for coin in coins:
        if total == 0:
            break
        count = total // coin  # Determine how many of this coin can fit into the total
        num_coins += count
        total -= count * coin  # Reduce the total by the value of coins used

    return num_coins if total == 0 else -1
