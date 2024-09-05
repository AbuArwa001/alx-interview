#!/usr/bin/env python3
"""
prime_game module
"""
def sieve_of_eratosthenes(max_n):
    """
    Returns a list of prime numbers up to max_n
    """
    is_prime = [True] * (max_n + 1)
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, max_n + 1) if is_prime[p]]
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the game
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        remaining = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben
        while True:
            move_made = False
            for prime in primes:
                if prime in remaining:
                    move_made = True
                    multiples = set(range(prime, n + 1, prime))
                    remaining -= multiples
                    break
            if not move_made:
                if turn == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            turn = 1 - turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
