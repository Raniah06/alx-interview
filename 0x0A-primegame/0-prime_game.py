#!/usr/bin/python3
"""
Prime Game module
"""


def is_prime(num):
    """
    Check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """
    Generate a list of primes up to n using the Sieve of Eratosthenes.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: The name of the player who won the most rounds (Maria or Ben).
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_counts = [0] * (max_num + 1)

    # Precompute the cumulative number of primes up to each number
    count = 0
    for i in range(1, max_num + 1):
        if i in primes:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 0:  # Ben wins if the count is even
            ben_wins += 1
        else:  # Maria wins if the count is odd
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
